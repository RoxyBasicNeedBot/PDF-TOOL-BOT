import logging
from typing import Any, Dict
from core.langs.eng import STRINGS as eng_strings
from core.langs.arb import STRINGS as arb_strings
from core.langs.hnd import STRINGS as hnd_strings
from core.langs.uzb import STRINGS as uzb_strings
from core.langs.spn import STRINGS as spn_strings
from core.langs.frn import STRINGS as frn_strings
from core.langs.ita import STRINGS as ita_strings
from core.langs.rus import STRINGS as rus_strings
from core.langs.chn import STRINGS as chn_strings
from core.langs.tur import STRINGS as tur_strings
from core.langs.prt import STRINGS as prt_strings
from core.langs.deu import STRINGS as deu_strings
from core.langs.jpn import STRINGS as jpn_strings
from core.langs.kor import STRINGS as kor_strings
from core.langs.fas import STRINGS as fas_strings
from core.langs.ben import STRINGS as ben_strings
from core.langs.tha import STRINGS as tha_strings

from ledger.safebox import db as safebox
from core.nexus import settings

logger = logging.getLogger(__name__)

LANGUAGES = {
    "eng": eng_strings,
    "arb": arb_strings,
    "hnd": hnd_strings,
    "uzb": uzb_strings,
    "spn": spn_strings,
    "frn": frn_strings,
    "ita": ita_strings,
    "rus": rus_strings,
    "chn": chn_strings,
    "tur": tur_strings,
    "prt": prt_strings,
    "deu": deu_strings,
    "jpn": jpn_strings,
    "kor": kor_strings,
    "fas": fas_strings,
    "ben": ben_strings,
    "tha": tha_strings,
}

LANG_MAP = {
    "eng": {"flag": "🇬🇧", "name": "English"},
    "arb": {"flag": "🇸🇦", "name": "عربي"},
    "hnd": {"flag": "🇮🇳", "name": "हिन्दी"},
    "uzb": {"flag": "🇺🇿", "name": "Uzbek"},
    "spn": {"flag": "🇪🇸", "name": "español"},
    "frn": {"flag": "🇫🇷", "name": "française"},
    "ita": {"flag": "🇮🇹", "name": "italiana"},
    "rus": {"flag": "🇷🇺", "name": "Русский"},
    "chn": {"flag": "🇨🇳", "name": "简体中文"},
    "tur": {"flag": "🇹🇷", "name": "Türkçe"},
    "prt": {"flag": "🇵🇹", "name": "Português"},
    "deu": {"flag": "🇩🇪", "name": "Deutsch"},
    "jpn": {"flag": "🇯🇵", "name": "日本語"},
    "kor": {"flag": "🇰🇷", "name": "한국어"},
    "fas": {"flag": "🇮🇷", "name": "فارسی"},
    "ben": {"flag": "🇧🇩", "name": "বাংলা"},
    "tha": {"flag": "🇹🇭", "name": "ไทย"},
}

def get_text(key: str, lang: str = "eng") -> Any:
    """
    Retrieve translation string or dict for the given key and language code.
    Falls back to English if the key is missing.
    """
    if not lang or lang not in LANGUAGES:
        lang = "eng"
    
    strings = LANGUAGES[lang]
    if key in strings:
        return strings[key]
    
    # Try alternate forms in selected language
    clean_k = key.lstrip('_')
    if clean_k in strings:
        return strings[clean_k]
    if f'_{key}' in strings:
        return strings[f'_{key}']
    
    # Fallback to English
    fallback_strings = LANGUAGES.get("eng", {})
    if key in fallback_strings:
        return fallback_strings[key]
    if clean_k in fallback_strings:
        return fallback_strings[clean_k]
    if f'_{key}' in fallback_strings:
        return fallback_strings[f'_{key}']
    
    logger.error(f"Translation key '{key}' not found in any language dictionary.")
    return f"[{key}]"

async def get_user_lang(user_id: int) -> str:
    """Fetch user's language code from DB, defaulting to settings.DEFAULT_LANG or 'eng'."""
    try:
        user_info = await safebox.get_user_data(user_id)
        if user_info and "lang" in user_info:
            return user_info["lang"]
        return settings.DEFAULT_LANG or "eng"
    except Exception as e:
        logger.error(f"Failed to fetch language for user {user_id}: {e}")
        return settings.DEFAULT_LANG or "eng"

async def set_user_lang(user_id: int, lang: str) -> bool:
    """Set user's language preference in DB."""
    try:
        if lang in LANGUAGES:
            user_info = await safebox.get_user_data(user_id)
            if user_info:
                # Update user info with new language
                await safebox.set_key(id=user_id, key="lang", value=lang)
            return True
        return False
    except Exception as e:
        logger.error(f"Failed to set language for user {user_id} to '{lang}': {e}")
        return False

import re
from typing import Tuple, Any

deBUTTON_SPLIT = 2

async def createBUTTON(btn: dict, order: int = deBUTTON_SPLIT) -> Any:
    from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    from core.corestate import myID
    from itertools import islice
    
    try:
        button = []
        for key, value in btn.items():
            if value.startswith(("https://", "http://")):
                username = myID[0].username if myID else ""
                temp = InlineKeyboardButton(key, url=value.format(username))
            else:
                temp = InlineKeyboardButton(key, callback_data=value)
            button.append(temp)
            
        if order == deBUTTON_SPLIT:
            keyboard = [button[i:i+deBUTTON_SPLIT] for i in range(0, len(button), deBUTTON_SPLIT)]
        else:
            new_order = [int(x) for x in str(order)]
            button_iter = iter(button)
            keyboard = [list(islice(button_iter, elem)) for elem in new_order]
            
        return InlineKeyboardMarkup(keyboard)
    except Exception as e:
        logger.error(f"Error in createBUTTON: {e}")
        return None

def _resolve(lang_code: str, expr: str) -> Any:
    if not expr:
        return None
    # e.g., SETTINGS['back'][1]
    match = re.match(r"^(\w+)\['([^']+)'\]\[(\d+)\]$", expr)
    if not match:
        match = re.match(r'^(\w+)\["([^"]+)"\]\[(\d+)\]$', expr)
    if match:
        var_name, key, idx = match.groups()
        from core.legacy_dicts import get_legacy_dict
        container = get_legacy_dict(var_name, lang_code)
        if isinstance(container, dict) and key in container:
            val = container[key]
            if isinstance(val, (list, tuple)) and len(val) > int(idx):
                return val[int(idx)]
        return f"[{expr}]"
    
    # e.g., INDEX['encrypt_caption']
    match = re.match(r"^(\w+)\['([^']+)'\]$", expr)
    if not match:
        match = re.match(r'^(\w+)\["([^"]+)"\]$', expr)
    if match:
        var_name, key = match.groups()
        from core.legacy_dicts import get_legacy_dict
        container = get_legacy_dict(var_name, lang_code)
        if isinstance(container, dict) and key in container:
            return container[key]
        return f"[{expr}]"
    
    # Direct attribute, e.g., HOME_A or INLINE
    from core.legacy_dicts import get_legacy_dict
    container = get_legacy_dict(expr, lang_code)
    if container:
        return container
    return get_text(expr, lang_code)

async def translate(
    text: str = None,
    button: dict = None,
    asString: bool = False,
    order: int = deBUTTON_SPLIT,
    lang_code: str = "eng",
) -> Tuple[Any, Any]:
    
    rtn_text = text
    rtn_button = button
    
    if text is not None:
        rtn_text = _resolve(lang_code, text)
        if rtn_text == f"[{text}]":
            rtn_text = _resolve("eng", text) # fallback
            
    if button is not None:
        if isinstance(button, str):
            rtn_button = _resolve(lang_code, button)
            if rtn_button == f"[{button}]":
                rtn_button = _resolve("eng", button)
        else:
            rtn_button = button
            
    if asString:
        return rtn_text, rtn_button
        
    if rtn_button is not None and isinstance(rtn_button, dict):
        return rtn_text, await createBUTTON(rtn_button, order)
        
    return rtn_text, rtn_button

async def getLang(chat_id: int) -> str:
    return await get_user_lang(chat_id)

def disLang(lang_code: str) -> str:
    if lang_code in LANG_MAP:
        return LANG_MAP[lang_code]['name']
    return LANG_MAP.get(settings.DEFAULT_LANG, LANG_MAP['eng'])['name']

async def editDICT(
    inDir: dict, value: Any = False, front: Any = False
) -> dict:
    outDir = {}

    if front:  # changes cb in UI
        for i, j in inDir.items():
            try:
                outDir[i.format(front)] = j
            except Exception:
                outDir[i] = j
        inDir = outDir

    if value and not isinstance(value, list):  # changes cb.data
        for i, j in inDir.items():
            try:
                outDir[i] = j.format(value)
            except Exception:
                outDir[i] = j
    
    elif value and isinstance(value, list):
        if len(value) == 2:
            for i, j in inDir.items():
                try:
                    outDir[i] = j.format(value[0], value[1])
                except Exception:
                    outDir[i] = j
        elif len(value) == 3:
            for i, j in inDir.items():
                try:
                    outDir[i] = j.format(value[0], value[1], value[2])
                except Exception:
                    outDir[i] = j
    
    if not outDir:
        return inDir
    return outDir
