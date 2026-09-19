# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import re
import logging
import cloudscraper
from .bhelper import Util
from pathlib import Path
from .fetcher import LibgenDownload
from bs4 import BeautifulSoup as bsoup
from typing import Awaitable, Callable, Optional, List, Dict

logg = logging.getLogger(__name__)

class Libgen:
    """
    Search client interface to search Library Genesis mirrors and retrieve book documents list.
    """
    def __init__(
        self, sort: str = "def", sort_mode: str = "DESC", result_limit: int = 25
    ) -> None:
        allowed_sort = ["def", "id", "author", "title", "publisher", "year", "pages", "language", "size", "extension"]
        if sort.lower() in allowed_sort:
            self.sort = sort.lower()
        else:
            raise ValueError(f"Invalid sort column. Must be one of: {allowed_sort}")
            
        if sort_mode.upper() in ["ASC", "DESC"]:
            self.sort_mode = sort_mode.upper()
        else:
            raise ValueError("sort_mode must be ASC or DESC")
            
        self.result_limit = result_limit
        self.fields = ["def", "title", "author", "series", "publisher", "year", "identifier", "language", "md5", "tags", "extension"]
        # Use HTTPS mirrors — HTTP port 80 is firewalled on Render, HTTPS reaches Cloudflare
        # cloudscraper automatically bypasses Cloudflare's bot challenge
        self.libgen_mirrors = ["https://libgen.lc", "https://libgen.st", "https://libgen.rs", "https://libgen.li"]
        self.current_url = self.libgen_mirrors[0]
        
        self.session = cloudscraper.create_scraper(
            browser={"browser": "chrome", "platform": "windows", "mobile": False}
        )
        self.session.cookies.set("lg_topic", "libgen", domain="libgen.rs", expires=None)

    async def search(
        self,
        query: str,
        search_field: str = "def",
        filters: dict = {},
        return_fields: list = []
    ) -> dict:
        """
        Execute search query across mirrors.
        """
        if not query or len(query.strip()) < 2:
            raise ValueError("Query must be at least 2 characters long")
            
        clean_field = search_field.lower()
        if clean_field not in self.fields:
            raise ValueError(f"Invalid search field. Must be one of: {self.fields}")

        req_param = "req=" + "+".join(query.strip().split(" "))
        col_param = f"column={clean_field}"
        sort_param = f"sort={self.sort}"
        mode_param = f"sortmode={self.sort_mode}"
        limit_param = f"res={self.result_limit}"

        search_endpoint = f"{self.current_url}/search.php?"
        compiled_url = "&".join([search_endpoint, req_param, limit_param, col_param, sort_param, mode_param])

        return await self._execute_search_flow(compiled_url, filters, return_fields)

    async def _execute_search_flow(self, url: str, filters: dict, return_fields: list) -> dict:
        ids_list = await self._fetch_ids(url)
        if not ids_list:
            return {}
        return await self._fetch_json_metadata(ids_list, return_fields, filters)

    async def _fetch_ids(self, url: str) -> list:
        last_err = None
        for mirror in self.libgen_mirrors:
            try:
                mirror_search_url = url.replace(self.current_url, mirror)
                resp = self.session.get(mirror_search_url, allow_redirects=True, timeout=12)
                
                if resp.status_code != 200:
                    continue
                
                soup = bsoup(resp.content, "lxml")
                table = soup.find("table", attrs={"rules": "rows"})
                if not table:
                    # HTTP 200 but no table (e.g., Cloudflare challenge or changed layout)
                    last_err = Exception(f"No data table found in {mirror}")
                    continue
                    
                self.current_url = mirror
                
                for tag in soup.findAll("script"):
                    tag.decompose()
                    
                rows = table.findAll("tr")[1:]
                return [tr.td.get_text(strip=True) for tr in rows if tr.td]
                
            except Exception as e:
                last_err = e
        else:
            if last_err:
                await Util.raise_error(0, f"All LibGen mirrors failed. Last error: {last_err}")
            else:
                await Util.raise_error(500, "All LibGen mirrors returned bad status codes")

    async def _fetch_json_metadata(self, ids_list: list, return_fields: list, filters: dict) -> dict:
        json_endpoint = f"{self.current_url}/json.php?"
        ids_param = "ids=" + ",".join(ids_list)
        
        fields_list = ["id"]
        if return_fields:
            if "mirrors" in return_fields:
                fields_list.extend(["md5", "sha1", "filesize", "edonkey", "aich", "tth", "extension"])
            fields_list.extend([f for f in return_fields if f != "mirrors"])
            fields_param = "fields=" + ",".join(set(fields_list))
        else:
            fields_param = "fields=*"

        query_url = "&".join([json_endpoint, ids_param, fields_param])
        resp = self.session.get(query_url, allow_redirects=True, timeout=12)
        
        if resp.status_code != 200:
            await Util.raise_error(resp.status_code, resp.reason)
            
        raw_json = resp.json()
        return await self._format_and_filter(raw_json, ids_list, filters, return_fields)

    async def _format_and_filter(self, raw_data: list, ids_list: list, filters: dict, return_fields: list) -> dict:
        formatted_data = {}
        if not raw_data:
            return {}
            
        for book_id in ids_list:
            match = next((item for item in raw_data if str(item.get("id")) == str(book_id)), None)
            if match:
                formatted_data[str(book_id)] = match

        filtered_keys = list(formatted_data.keys())
        for r_id in filtered_keys:
            item = formatted_data[r_id]
            if filters:
                if not await Util.filter_result(item, filters):
                    formatted_data.pop(r_id)
                    continue

            # Cover Image resolver
            cover_regex = re.compile(r"^\d+\\?\/[a-z-0-9]+\..{1,4}$", re.IGNORECASE)
            cover = item.get("coverurl", "")
            if cover:
                if re.match(cover_regex, cover):
                    item["coverurl"] = f"{self.current_url}/covers/{cover}"
                else:
                    item["coverurl"] = "https://cdn2.iconfinder.com/data/icons/leto-blue-online-education/64/__book_mouth_education_online-512.png"

            # Mirror links resolver
            if not return_fields or "mirrors" in return_fields:
                md5 = item.get("md5", "")
                sha1 = item.get("sha1", "")
                size = item.get("filesize", 0)
                edonkey = item.get("edonkey", "")
                aich = item.get("aich", "")
                tth = item.get("tth", "")
                ext = item.get("extension", "")

                # Pop fields if not requested explicitly
                if return_fields:
                    for f in ["md5", "sha1", "filesize", "edonkey", "aich", "tth", "extension"]:
                        if f not in return_fields and f in item:
                            item.pop(f)

                tor_num = str(r_id)[:-3] + "000" if int(r_id) >= 1000 else "000"
                item["mirrors"] = {
                    "main": f"http://library.lol/main/{md5}",
                    "libgen.lc": f"http://libgen.lc/ads.php?md5={md5}",
                    "z-library": f"http://b-ok.cc/md5/{md5}",
                    "libgen.pw": f"https://libgen.pw/item?id={r_id}",
                    "bookfi": f"http://bookfi.net/md5/{md5}",
                    "torrent": f"{self.current_url}/book/index.php?md5={md5}&oftorrent=",
                    "torrent_1k": f"{self.current_url}/repository_torrent/r_{tor_num}.torrent",
                    "gnutella": f"magnet:?xt=urn:sha1:{sha1}&xl={size}&dn={md5}.{ext}",
                    "ed2k": f"ed2k://|file|{md5.upper()}.{ext}|{size}|{edonkey}|h={aich}|/",
                    "dc++": f"magnet:?xt=urn:tree:tiger:{tth}&xl={size}&dn={md5}.{ext}"
                }

            if "torrent" in item:
                item.pop("torrent")
            if "locator" in item:
                item.pop("locator")
            if "id" in item:
                item.pop("id")

        return formatted_data

    @staticmethod
    async def download(
        url: str,
        dest_folder: Path = None,
        progress: Optional[Callable[..., Awaitable[None]]] = None,
        progress_args: list = []
    ) -> Path:
        """
        Download book from resolved mirror URL.
        """
        return await LibgenDownload().download(url, dest_folder, progress, progress_args)
