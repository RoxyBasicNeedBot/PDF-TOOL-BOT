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

from pyrogram import filters

class CommandRegistry:
    ALL_COMMANDS = [
        'start', 'help', 'cancel', 'delete', 'beta',
        'donate', 'ban', 'unban', 'stop', 'send',
        'set', 'txt2pdf', 'hd'
    ]

    @classmethod
    def get_command_filter(cls):
        return filters.command(cls.ALL_COMMANDS)

    @classmethod
    def get_non_command_filter(cls):
        return ~filters.command(cls.ALL_COMMANDS)

    @classmethod
    def get_command_list(cls):
        return cls.ALL_COMMANDS.copy()

def get_command_filter():
    return CommandRegistry.get_command_filter()

def get_non_command_filter():
    return CommandRegistry.get_non_command_filter()

def get_command_list():
    return CommandRegistry.get_command_list()
