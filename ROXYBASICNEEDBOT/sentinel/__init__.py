# ┌─────────────────────────────────────────────────────────────┐
# │                    𝕽𝕺𝕏𝖄•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │  Created by: RoxyBasicNeedBot                               │
# │  GitHub    : https://github.com/RoxyBasicNeedBot            │
# │  Telegram  : https://t.me/roxybasicneedbot1                 │
# │  Website   : https://roxybasicneedbot.unaux.com             │
# │  YouTube   : @roxybasicneedbot                              │
# ├─────────────────────────────────────────────────────────────┤
# │      Bot Developer, Automation Architect & Python Coder      │
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

from .guardian import safe_send, safe_reply_text
from .gatepass import stop_bot, banned_user, banned_group, set_db, not_subscribed, extract_data
from .dialogstream import ask, setup_conversation_handler
from .workspace import work
from .thumbcaster import thumbMeta, formatThumb, thumbName
from .talkback import caption
from .ramguard import check_memory_for_file, force_cleanup, get_available_memory_mb, get_memory_usage_percent
from .render import header, ensure_reply_to_message, gSF, checkPdf, progress, _progress, cbPRO
from .cmdvault import set_bot_commands
from .cmdlist import get_command_filter, get_non_command_filter, get_command_list
from core.i18n import translate, getLang, createBUTTON, editDICT

# Alias util to match v1 imports
class UtilAlias:
    def __getattr__(self, name):
        if name in globals():
            return globals()[name]
        import core.i18n as trans
        import sentinel.thumbcaster as tc
        if hasattr(trans, name):
            return getattr(trans, name)
        if hasattr(tc, name):
            return getattr(tc, name)
        raise AttributeError(f"module sentinel has no attribute {name}")

util = UtilAlias()
