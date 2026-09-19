import logging
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from core.i18n import LANG_MAP, get_text, set_user_lang, get_user_lang
from ledger.safebox import db as safebox
from core.nexus import settings

logger = logging.getLogger(__name__)

def get_language_keyboard():
    """Generates the inline keyboard for language selection."""
    buttons = []
    # Build 2-column layout
    lang_keys = list(LANG_MAP.keys())
    for i in range(0, len(lang_keys), 2):
        row = []
        # First column
        code_1 = lang_keys[i]
        info_1 = LANG_MAP[code_1]
        row.append(InlineKeyboardButton(f"{info_1['flag']} {info_1['name']}", callback_data=f"setlang_{code_1}"))
        
        # Second column (if exists)
        if i + 1 < len(lang_keys):
            code_2 = lang_keys[i + 1]
            info_2 = LANG_MAP[code_2]
            row.append(InlineKeyboardButton(f"{info_2['flag']} {info_2['name']}", callback_data=f"setlang_{code_2}"))
            
        buttons.append(row)
        
    return InlineKeyboardMarkup(buttons)

@Client.on_message(filters.command("lang") & filters.private)
async def lang_command(client: Client, message: Message):
    """Handler for the /lang command to select language."""
    if not getattr(settings, "MULTI_LANG_SUP", True):
        return await message.reply_text("❌ Multi-Language Support is disabled by the admin.")
    user_id = message.from_user.id
    user_lang = await get_user_lang(user_id)
    
    # We use LANGUAGE directly from the bot's strings
    text = get_text("LANGUAGE", user_lang)
    if isinstance(text, str):
        # Adding a descriptive message just like devgagan
        text = "🌍 **Please choose your language:**\n\nSelect one of the options below to proceed."
        
    keyboard = get_language_keyboard()
    
    await message.reply_text(
        text=text,
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.MARKDOWN
    )

@Client.on_callback_query(filters.regex(r"^setlang_(\w+)"))
async def setlang_callback(client: Client, callback_query: CallbackQuery):
    """Callback query handler for setting the user's language."""
    user_id = callback_query.from_user.id
    lang_code = callback_query.matches[0].group(1)
    
    if lang_code not in LANG_MAP:
        await callback_query.answer("❌ Invalid language option selected.", show_alert=True)
        return
        
    # Update language in DB
    success = await set_user_lang(user_id, lang_code)
    if not success:
        await callback_query.answer("❌ Failed to update language preference.", show_alert=True)
        return
        
    # Get confirmation text in the newly selected language
    confirm_text = get_text("LANG_FEED", lang_code)
    
    # Notify user via alert
    if type(confirm_text) is str:
        # We format it if it has {} for language name
        if "{}" in confirm_text:
            confirm_text = confirm_text.format(LANG_MAP[lang_code]['name'])
    else:
        confirm_text = "✅ Language configured successfully!"
        
    # Telegram max alert length is 200 chars
    alert_text = confirm_text.replace("**", "").replace("✅ ", "")[:190]
    await callback_query.answer(alert_text, show_alert=True)
    
    # After choosing the language, edit the message to show the normal home screen in their chosen language
    try:
        user_first_name = callback_query.from_user.first_name
        # Re-fetch home text
        home_text = get_text("HOME_A", lang_code)
        if type(home_text) is str and "{}" in home_text:
            # HOME_A usually expects 2 args: format(user_first_name, client.me.first_name)
            # but we'll safely format it
            try:
                home_text = home_text.format(user_first_name, client.me.first_name)
            except Exception:
                home_text = home_text.replace("{}", user_first_name, 1).replace("{}", client.me.first_name, 1)

        # Build standard home keyboard
        keyboard_map = get_text("DOCUMENT", lang_code)
        keyboard = None
        if isinstance(keyboard_map, dict) and "_replyCB" in keyboard_map:
            # We reconstruct the replyCB
            pass
            
        # The user just wants the interface of language updated, we can just delete the menu or show a simple back to home
        back_btn = get_text("BACK_HOME", lang_code)
        if not isinstance(back_btn, str): back_btn = "🔙 Back to Home"
        
        markup = InlineKeyboardMarkup([[InlineKeyboardButton(back_btn, callback_data="home")]])
        await callback_query.message.edit_text(text=home_text, reply_markup=markup)
    except Exception as e:
        logger.error(f"Error editing language picker message: {e}")
        await callback_query.message.delete()
