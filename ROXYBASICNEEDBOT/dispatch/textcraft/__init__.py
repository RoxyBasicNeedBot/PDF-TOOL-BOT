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

class ModuleMeta:
    FILE_PATH = "ROXYBASICNEEDBOT/modules/dm/textToPdf/__init__.py"
    AUTHOR = "roxybasicneedbot"
    TELEGRAM = "telegram.dog/roxybasicneedbot"
    LICENSE = "Copyright © 2026, roxybasicneedbot"

file_name = ModuleMeta.FILE_PATH
__author__ = ModuleMeta.AUTHOR


'''
██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗  ██████╗ ████████╗
██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ██████╔╝██║   ██║   ██║   
██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ██╔═══╝ ██║   ██║   ██║   
██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ██║     ╚██████╔╝   ██║   
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝    ╚═╝   
                  ⚡ Powering Automation ⚡
'''

path = "plugins/dm/textToPdf"

TXT = {}

SCALE = { 1: "Landscape", 2: "Portrait" }

# FONT PREVIEW: https://graph.org/roxy-pdftool-06-15
FONT = {
    1: f"{path}/FONT_LIBRARY/DejaVuSans.ttf",
    2: f"{path}/FONT_LIBRARY/WinterSong-owRGB.ttf",
    3: f"{path}/FONT_LIBRARY/Conquest-8MxyM.ttf",
    4: f"{path}/FONT_LIBRARY/Branda-yolq.ttf",
    5: f"{path}/FONT_LIBRARY/ArianaVioleta-dz2K.ttf",
    6: f"{path}/FONT_LIBRARY/3Dumb.ttf",
    7: f"{path}/FONT_LIBRARY/AlexBrush-Regular.ttf",
    8: f"{path}/FONT_LIBRARY/Archistico_Bold.ttf",
    9: f"{path}/FONT_LIBRARY/Archistico_Simple.ttf",
    10: f"{path}/FONT_LIBRARY/Calligraffiti.ttf",
    11: f"{path}/FONT_LIBRARY/DancingScript-Regular.otf",
    12: f"{path}/FONT_LIBRARY/FFF_Tusj.ttf",
    13: f"{path}/FONT_LIBRARY/GreatVibes-Regular.otf",
    14: f"{path}/FONT_LIBRARY/Kristi.ttf",
    15: f"{path}/FONT_LIBRARY/Pacifico.ttf",
}

COLOR = {
    1: {"color": "black", "code": (0, 0, 0)},
    2: {"color": "grey", "code": (128, 128, 128)},
    3: {"color": "white", "code": (255, 255, 255)},
    4: {"color": "red", "code": (255, 0, 0)},
    5: {"color": "green", "code": (0, 255, 0)},
    6: {"color": "blue", "code": (0, 0, 255)},
}

BACKGROUND_L = {
    1: {"isColor": True, "code": (255, 255, 255), "position": ["w", 20, "w", 10]},
    2: {
        "isColor": False,
        "code": f"{path}/IMAGES/black.png",
        "position": ["w", 20, "w", 10],
    },
    3: {"isColor": True, "code": (128, 128, 128), "position": ["w", 20, "w", 10]},
    4: {
        "isColor": False,
        "code": f"{path}/IMAGES/sanscrit.png",
        "position": ["w", 20, "w", 10],
    },
    5: {
        "isColor": False,
        "code": f"{path}/IMAGES/folded.png",
        "position": ["w", 20, "w", 10],
    },
}

BACKGROUND_P = {
    1: {"isColor": True, "code": (255, 255, 255), "position": ["w", 20, "w", 10]},
    2: {
        "isColor": False,
        "code": f"{path}/IMAGES/black.png",
        "position": ["w", 20, "w", 10],
    },
    3: {"isColor": True, "code": (128, 128, 128), "position": ["w", 20, "w", 10]},
    4: {
        "isColor": False,
        "code": f"{path}/IMAGES/sanscrit.png",
        "position": ["w", 20, "w", 10],
    },
    5: {
        "isColor": False,
        "code": f"{path}/IMAGES/folded.png",
        "position": ["w", 20, "w", 10],
    },
}

_all__ = [
    'TXT',
    'SCALE',
    'FONT',
    'COLOR',
    'BACKGROUND_L',
    'BACKGROUND_P',
]