# ┌─────────────────────────────────────────────────────────────┐
# │                    𕲏𕲏𕲏𕲏•𝔹𝕒𝕤𝕚𝕔ℕ𝕖𝕖𝕕𝔹𝕠𝕥                     │
# │            The Ultimate Telegram PDF Suite Tool             │
# ├─────────────────────────────────────────────────────────────┤
# │        © 2026 RoxyBasicNeedBot. All Rights Reserved.        │
# └─────────────────────────────────────────────────────────────┘

"""
Repository synchronization utility to fetch updates from upstream main remote branches automatically.
"""

import os
import subprocess
import dotenv
from tracer import logger

class UpstreamRepositorySyncer:
    def __init__(self):
        for env_file in ["config.env", "../config.env", ".env", "../.env"]:
            if os.path.exists(env_file):
                dotenv.load_dotenv(env_file, override=False)
        self.upstream_repo = os.getenv("upstream_repo")
        self.upstream_branch = os.getenv("upstream_branch", "main")

    def synchronize(self) -> bool:
        """
        Check environment flags, clean git configurations and reset repository hard to origin.
        """
        if not self.upstream_repo:
            logger.info("No upstream repository configured for sync.")
            return False

        logger.info(f"Syncing with upstream repository: {self.upstream_repo} on branch: {self.upstream_branch}")
        
        # Clean local git directory if corrupted
        if os.path.exists(".git"):
            try:
                subprocess.run(["rm", "-rf", ".git"], check=True)
            except Exception:
                pass

        try:
            # Initialize clean repository, stage files, and sync hard from origin
            cmds = [
                "git init -q",
                "git add .",
                'git commit -sm "sync backup" -q',
                f"git remote add origin {self.upstream_repo}",
                "git fetch origin -q",
                f"git reset --hard origin/{self.upstream_branch} -q"
            ]
            
            result = subprocess.run(" && ".join(cmds), shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                logger.info(f"Repository successfully synchronized with upstream commit from {self.upstream_branch}!")
                return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Synchronization process failed: {e.stderr.decode('utf-8', errors='ignore')}")
        except Exception as e:
            logger.error(f"Unexpected sync error: {e}")
        return False

if __name__ == "__main__":
    syncer = UpstreamRepositorySyncer()
    syncer.synchronize()