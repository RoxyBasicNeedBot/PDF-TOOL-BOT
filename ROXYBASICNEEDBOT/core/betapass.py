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

class BetaPass:
    def __init__(self):
        self._testers = []

    def extend(self, users):
        self._testers.extend(users)

    def append(self, user):
        if user not in self._testers:
            self._testers.append(user)

    def remove(self, user):
        if user in self._testers:
            self._testers.remove(user)

    def __contains__(self, user):
        return user in self._testers

    def __len__(self):
        return len(self._testers)

    def __iter__(self):
        return iter(self._testers)

BETA = BetaPass()
