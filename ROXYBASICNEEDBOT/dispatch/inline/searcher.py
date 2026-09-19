# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𕕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from . import *
from core.nexus import settings
from .fallback import default_ans, search
file_name = "ROXYBASICNEEDBOT/dispatch/inline/searcher.py"
from pyrogram.types import (
    InlineQueryResultPhoto,
    InlineQueryResultCachedDocument,
)
import aiohttp
import urllib.parse


FALLBACK_COVER = "https://te.legra.ph/file/8dfa3760df91a218a629c.jpg"


async def search_internet_archive(query: str, limit: int = 25) -> list:
    """
    Search Internet Archive for books. Returns a list of dicts.
    """
    params = {
        "q": f"{query} AND mediatype:texts",
        "fl[]": "identifier,title,creator,year,downloads,mediatype,format,language,publisher",
        "rows": limit,
        "page": 1,
        "output": "json"
    }
    url = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(params, doseq=True)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
            if resp.status != 200:
                return []
            data = await resp.json()

    books = []
    for doc in data.get("response", {}).get("docs", []):
        identifier = doc.get("identifier", "")
        if not identifier:
            continue
            
        cover_url = f"https://archive.org/services/img/{identifier}"
        
        title = doc.get("title", "Unknown")
        
        creators = doc.get("creator", [])
        if isinstance(creators, list):
            author = ", ".join(creators[:2]) if creators else "Unknown"
        else:
            author = str(creators)
            
        year = str(doc.get("year", "N/A"))
        
        langs = doc.get("language", [])
        lang = langs[0] if isinstance(langs, list) and langs else str(langs) if langs else "English"
        
        publishers = doc.get("publisher", [])
        publisher = publishers[0] if isinstance(publishers, list) and publishers else str(publishers) if publishers else "N/A"

        books.append({
            "title": title,
            "author": author,
            "year": year,
            "pages": "N/A", # IA doesn't readily provide page count in basic search
            "publisher": publisher,
            "cover_url": cover_url,
            "identifier": identifier,
            "language": lang
        })

    return books


@RoxyBot.on_inline_query()
async def inline_query_handler(bot, inline_query):
    try:
        query = inline_query.query.strip()
        results = []

        lang_code = await getLang(inline_query.from_user.id)
        trCHUNK, _ = await translate(text="INLINE", lang_code=lang_code)

        # Check if inline search feature is enabled
        if not settings.INLINE_SEARCH:
            result = await default_ans(inline_query)
            return await inline_query.answer(
                results=result,
                cache_time=0,
                switch_pm_text="⚠️ Inline search is disabled",
                switch_pm_parameter="okay",
            )

        # Inline feature will not work if there is no log channel set up.
        if not log.LOG_CHANNEL:
            result = await default_ans(inline_query)
            return await inline_query.answer(
                results=result,
                cache_time=0,
                switch_pm_text=trCHUNK["noDB"],
                switch_pm_parameter="okay",
            )

        elif len(query) < 2:
            result = await default_ans(inline_query)
            return await inline_query.answer(
                results=result,
                cache_time=0,
                switch_pm_text=trCHUNK["min"],
                switch_pm_parameter="okay",
            )

        elif "|" in query:
            result = await search(inline_query)
            return await inline_query.answer(
                results=result, cache_time=0, switch_pm_text=""
            )

        else:
            if query:
                try:
                    books = await search_internet_archive(query, limit=50)
                except Exception as search_error:
                    import traceback
                    logger.error(f"🐞 Internet Archive search failed: {search_error}")
                    logger.error(f"🐞 Traceback:\n{traceback.format_exc()}")
                    result = await default_ans(inline_query)
                    return await inline_query.answer(
                        results=result,
                        cache_time=0,
                        switch_pm_text="❌ Search service temporarily unavailable",
                        switch_pm_parameter="okay",
                    )

                if books:
                    DATA[inline_query.from_user.id] = {}
                    for idx, book in enumerate(books, start=1):
                        title = book["title"]
                        author = book["author"]
                        year = book["year"]
                        pages = book["pages"]
                        publisher = book["publisher"]
                        cover_url = book["cover_url"]
                        identifier = book["identifier"]
                        lang = book.get("language", "English")

                        # Deep link for downloading from Internet Archive
                        deeplink = f"-ia{identifier}"


                        results.append(
                            InlineQueryResultPhoto(
                                photo_url=cover_url,
                                title=title,
                                id=f"{idx}",
                                description=trCHUNK["description"].format(
                                    author, "", year, pages, lang, "pdf", publisher,
                                ),
                                caption=trCHUNK["caption"].format(
                                    identifier, title, author, "", year, pages, lang, publisher,
                                ),
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [
                                            InlineKeyboardButton(
                                                text=trCHUNK["select"],
                                                url=f"https://t.me/{myID[0].username}?start={deeplink}",
                                            )
                                        ]
                                    ]
                                ),
                            )
                        )
                        DATA[inline_query.from_user.id][idx] = {
                            "thumb": cover_url,
                            "caption": f"ID: {identifier}\nTitle: **{title}.**\nAuthor: **{author}.**",
                        }

        if results:
            return await inline_query.answer(
                results=results,
                cache_time=60,
                is_personal=False,
                switch_pm_text=trCHUNK["query"].format(len(results)),
                switch_pm_parameter="okey",
            )
        else:
            result = await default_ans(inline_query)
            return await inline_query.answer(
                results=result,
                cache_time=0,
                switch_pm_text=trCHUNK["nothing"].format(query),
                switch_pm_parameter="okay",
            )

    except errors.QueryIdInvalid:
        pass
    except Exception as e:
        logger.error("🐞 %s: %s" % (file_name, e), exc_info=True)

