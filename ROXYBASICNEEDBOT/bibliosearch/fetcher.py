# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

import re
import time
import aiohttp
import aiofiles
import logging
import requests
from .bhelper import Util
from pathlib import Path
from tldextract import extract
from bs4 import BeautifulSoup as bsoup
from typing import Awaitable, Callable, Optional

logg = logging.getLogger(__name__)

class LibgenDownload:
    """
    Downloader interface to resolve Libgen mirror direct links and stream files async.
    """
    def __init__(self) -> None:
        self.dest_folder = Path.cwd()
        self.mirrors = ["library.lol", "libgen.lc", "libgen.gs", "b-ok.cc"]
        self.url_regex = re.compile(
            r"^(?:http|ftp)s?://"
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
            r"(?::\d+)?"
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE
        )

    async def download(
        self,
        url: str,
        dest_folder: Path = None,
        progress: Optional[Callable[..., Awaitable[None]]] = None,
        progress_args: list = []
    ) -> Path:
        """
        Download a book from the specified Libgen mirror page URL.
        """
        domain_suffix = str(extract(url).domain) + "." + str(extract(url).suffix)
        if not re.match(self.url_regex, url) or domain_suffix not in self.mirrors:
            raise ValueError(f"Supported mirrors: {' - '.join(self.mirrors)}")

        if not dest_folder:
            dest_folder = self.dest_folder
        dest_path = Path(dest_folder)
        dest_path.mkdir(parents=True, exist_ok=True)

        direct_links = await self.get_directlink(url)
        for link in direct_links:
            downloaded_file = await self._stream_file(link, dest_path, progress, progress_args)
            if downloaded_file:
                return downloaded_file
        return None

    @staticmethod
    async def _stream_file(
        url: str,
        dest_folder: Path,
        progress: Optional[Callable[..., Awaitable[None]]],
        progress_args: list
    ) -> Optional[Path]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        return None
                        
                    content_length = response.headers.get("Content-Length")
                    total_size = int(content_length) if content_length else "Unknown size"
                    
                    filename = await Util.get_filename(response.headers.get("Content-Disposition"))
                    file_path = dest_folder.joinpath(filename)

                    async with aiofiles.open(file_path, mode="wb") as f:
                        downloaded_bytes = 0
                        start_time = time.time()
                        
                        async for chunk, _ in response.content.iter_chunks():
                            await f.write(chunk)
                            downloaded_bytes += len(chunk)
                            current_time = time.time()
                            
                            if current_time - start_time > 1.2:
                                if progress:
                                    await progress(downloaded_bytes, total_size, *progress_args)
                                start_time = current_time
                                
            return file_path
        except Exception as e:
            logg.error(f"Download streaming exception: {e}")
            return None

    async def get_directlink(self, url: str) -> list:
        """
        Parse Mirror page and return direct book download links.
        """
        tld_info = extract(url)
        r = requests.get(url, allow_redirects=True, timeout=15)
        if r.status_code != 200:
            await Util.raise_error(r.status_code, r.reason)

        soup = bsoup(r.content, "lxml")
        for tag in soup.findAll("script"):
            tag.decompose()

        domain = f"{tld_info.domain}.{tld_info.suffix}"
        direct_links = []
        
        if domain == "library.lol":
            div = soup.find("div", attrs={"id": "download"})
            if div and div.h2 and div.h2.a:
                direct_links.append(div.h2.a["href"])
            if div and div.ul:
                for li in div.ul.findAll("li"):
                    if li.a:
                        direct_links.append(li.a["href"])
                        
        elif domain in ["libgen.lc", "libgen.gs"]:
            table = soup.find("table", attrs={"id": "main"})
            if table and table.tr:
                tds = table.tr.findAll("td")
                if len(tds) > 1 and tds[1].a:
                    direct_links.append(tds[1].a["href"])
                    
        elif domain == "b-ok.cc":
            table = soup.find("table", attrs={"class": "resItemTable"})
            if table and table.tr:
                tds = table.tr.findAll("td")
                if len(tds) > 1 and tds[1].table and tds[1].table.tr.td.h3.a:
                    book_page = "http://b-ok.cc" + str(tds[1].table.tr.td.h3.a["href"])
                    book_resp = requests.get(book_page, allow_redirects=True, timeout=15)
                    if book_resp.status_code != 200:
                        await Util.raise_error(book_resp.status_code, book_resp.reason)
                        
                    book_soup = bsoup(book_resp.content, "lxml")
                    dl_button = book_soup.find("a", attrs={"class": "btn btn-primary dlButton addDownloadedBook"})
                    if dl_button:
                        direct_links.append(dl_button["href"])
            else:
                await Util.raise_error(0, "Book not found on mirror website")
                
        return direct_links
