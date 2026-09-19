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

import asyncio
from core.nexus import settings
from pyrogram import Client as RoxyBot, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice
from tracer import logger

DONATION_OPTIONS = {
    "small": {"stars": 10, "label": "☕ Small Coffee", "emoji": "☕"},
    "medium": {"stars": 25, "label": "☕☕ Medium Coffee", "emoji": "☕☕"},
    "large": {"stars": 50, "label": "☕☕☕ Large Coffee", "emoji": "☕☕☕"},
}

@RoxyBot.on_message(filters.private & filters.incoming & filters.command(["donate"]), group=0)
async def donate_command(bot_client: RoxyBot, message):
    logger.debug(f"💰 /donate command received from user {message.from_user.id}")
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                f"{DONATION_OPTIONS['small']['label']} ({DONATION_OPTIONS['small']['stars']}⭐)",
                callback_data="donate|small"
            )],
            [InlineKeyboardButton(
                f"{DONATION_OPTIONS['medium']['label']} ({DONATION_OPTIONS['medium']['stars']}⭐)",
                callback_data="donate|medium"
            )],
            [InlineKeyboardButton(
                f"{DONATION_OPTIONS['large']['label']} ({DONATION_OPTIONS['large']['stars']}⭐)",
                callback_data="donate|large"
            )],
            [InlineKeyboardButton("🚶 Close 🚶", callback_data="close|mee")]
        ])
        
        await message.reply_text(
            "<blockquote><b>☕ Support the Bot ☕</b></blockquote>\n\n"
            "<blockquote>Your donation helps keep this bot running and improving!</blockquote>\n\n"
            "Choose an option below to donate using <b>Telegram Stars</b>:",
            reply_markup=keyboard
        )
    except Exception as e:
        logger.error(f"Error in donate_command: {e}", exc_info=True)

@RoxyBot.on_callback_query(filters.regex("^donate\\|"))
async def donate_callback(bot_client: RoxyBot, callbackQuery):
    try:
        _, option = callbackQuery.data.split("|")
        
        if option not in DONATION_OPTIONS:
            return await callbackQuery.answer("Invalid option", show_alert=True)
        
        donation = DONATION_OPTIONS[option]
        user_id = callbackQuery.from_user.id
        
        await callbackQuery.answer("Creating invoice...")
        
        await bot_client.send_invoice(
            chat_id=user_id,
            title=f"{donation['label']}",
            description=f"Donate {donation['stars']} Stars to support the bot!",
            payload=f"donate|{option}|{user_id}",
            currency="XTR",
            prices=[LabeledPrice(label=donation['label'], amount=donation['stars'])]
        )
    except Exception as e:
        logger.error(f"Error in donate_callback: {e}", exc_info=True)
        await callbackQuery.answer("Error creating invoice. Please try again.", show_alert=True)

@RoxyBot.on_callback_query(filters.regex("^coffeeBtn$"))
async def coffee_button_callback(bot_client: RoxyBot, callbackQuery):
    try:
        await callbackQuery.answer()
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                f"{DONATION_OPTIONS['small']['label']} ({DONATION_OPTIONS['small']['stars']}⭐)",
                callback_data="donate|small"
            )],
            [InlineKeyboardButton(
                f"{DONATION_OPTIONS['medium']['label']} ({DONATION_OPTIONS['medium']['stars']}⭐)",
                callback_data="donate|medium"
            )],
            [InlineKeyboardButton(
                f"{DONATION_OPTIONS['large']['label']} ({DONATION_OPTIONS['large']['stars']}⭐)",
                callback_data="donate|large"
            )],
            [InlineKeyboardButton("🚶 Close 🚶", callback_data="close|mee")]
        ])
        
        await callbackQuery.edit_message_text(
            "<blockquote><b>☕ Support the Bot ☕</b></blockquote>\n\n"
            "<blockquote>Your donation helps keep this bot running and improving!</blockquote>\n\n"
            "Choose an option below to donate using <b>Telegram Stars</b>:",
            reply_markup=keyboard
        )
    except Exception as e:
        logger.error(f"Error in coffee_button_callback: {e}", exc_info=True)

@RoxyBot.on_pre_checkout_query()
async def pre_checkout_handler(bot_client: RoxyBot, pre_checkout_query):
    try:
        logger.debug(f"💳 Pre-checkout from user {pre_checkout_query.from_user.id}")
        await pre_checkout_query.answer(ok=True)
    except Exception as e:
        logger.error(f"Error in pre_checkout: {e}", exc_info=True)
        await pre_checkout_query.answer(ok=False, error_message="Payment error. Please try again.")

@RoxyBot.on_message(filters.successful_payment)
async def successful_payment_handler(bot_client: RoxyBot, message):
    try:
        payment = message.successful_payment
        payload = payment.invoice_payload
        total_amount = payment.total_amount
        transaction_id = payment.telegram_payment_charge_id
        
        logger.info(f"💰 Successful donation: {total_amount} Stars from user {message.from_user.id}")
        
        await message.reply_text(
            f"<blockquote><b>🎉 Thank You for Your Donation! 🎉</b></blockquote>\n\n"
            f"<b>Amount:</b> {total_amount} ⭐\n"
            f"<b>Transaction ID:</b> <code>{transaction_id}</code>\n\n"
            f"<blockquote>Your support means a lot and helps keep this bot running! ❤️</blockquote>"
        )
        
        try:
            await bot_client.send_message(
                chat_id=settings.OWNER_ID,
                text=f"<blockquote><b>💰 New Donation Received!</b></blockquote>\n\n"
                     f"<b>From:</b> {message.from_user.mention} (<code>{message.from_user.id}</code>)\n"
                     f"<b>Amount:</b> {total_amount} ⭐\n"
                     f"<b>Transaction ID:</b> <code>{transaction_id}</code>\n"
                     f"<b>Payload:</b> <code>{payload}</code>"
             )
        except Exception as e:
            logger.warning(f"Could not notify owner about donation: {e}")
            
    except Exception as e:
        logger.error(f"Error in successful_payment_handler: {e}", exc_info=True)
