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

import logging
import os
import sys

class RoxyLogger:
    def __init__(self, name="RoxyBot"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Check if handlers already exist to prevent duplicates
        if not self.logger.handlers:
            formatter = logging.Formatter(
                "[%(asctime)s - %(levelname)s - %(name)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            
            # Console Handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
            
            # File Handler
            log_dir = "logs"
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            file_handler = logging.FileHandler(os.path.join(log_dir, "roxybot.log"), encoding="utf-8")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

# Global logger instance
logger = RoxyLogger().get_logger()
tracer = logger

import builtins
builtins.logger = logger
builtins.tracer = tracer

# Visual banner for start
roxyBotBanner = """
██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗  ██████╗ ████████╗
██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ██████╔╝██║   ██║   ██║   
██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ██╔═══╝ ██║   ██║   ██║   
██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ██║     ╚██████╔╝   ██║   
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝    ╚═╝   
                  ⚡ Powering Automation v2 ⚡
"""
