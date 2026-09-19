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

from flask import Flask, jsonify, request
import os
import threading
from tracer import logger

class WebKeeper:
    def __init__(self):
        self.app = Flask("RoxyWebKeeper")
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route('/')
        def home():
            return jsonify({
                "status": "alive",
                "service": "RoxyBasicNeedBot PDF Suite",
                "uptime_monitor": "enabled"
            })

        @self.app.route('/ping')
        def ping():
            return 'pong', 200

        @self.app.route('/webhook/bridge/<token>', methods=['POST'])
        def webhook_bridge(token):
            # This endpoint receives cross-bot calls/PDFs from other bots using aiogram
            from core.nexus import bot
            expected_token = os.environ.get("BRIDGE_TOKEN") or bot.API_TOKEN
            if token != expected_token:
                return jsonify({"error": "Unauthorized"}), 403
                
            try:
                # Handle incoming JSON updates and push to aiogram bridge pipeline
                data = request.get_json(force=True)
                # In Phase 4, we will register the actual update handlers
                logger.info(f"Received bridge webhook event: {data.get('type')}")
                return jsonify({"status": "received"}), 200
            except Exception as e:
                logger.error(f"Error handling bridge webhook: {e}")
                return jsonify({"error": str(e)}), 500

    def start_async(self):
        def run():
            port = int(os.environ.get("PORT", 8080))
            logger.info(f"Starting pulse health server on port {port}")
            self.app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
            
        threading.Thread(target=run, daemon=True).start()

app = WebKeeper().app
