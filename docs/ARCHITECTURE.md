# 🏗️ RoxyBasicNeedBot v2 — Technical Architecture & Internals

<div align="center">
  <h3>Under the Hood: Concurrency Model, Multi-Engine Pipeline & B2B Relays</h3>
</div>

---

## 🏛️ High-Level System Architecture

```
                               ┌────────────────────────────────┐
                               │       Telegram Cloud MTProto   │
                               └────────────────────────────────┘
                                               │
                                               ▼
                              ┌─────────────────────────────────┐
                              │    Kurigram Asynchronous Client │
                              │    (20 Workers / 20 Transports) │
                              └─────────────────────────────────┘
                                               │
               ┌───────────────────────────────┴───────────────────────────────┐
               ▼                                                               ▼
  ┌─────────────────────────┐                                     ┌─────────────────────────┐
  │  Sentinel Security Gate │                                     │ aiogram 3 B2B Bridge    │
  │  (Flood, Memory, Auth)  │                                     │ (Cross-bot Updates API) │
  └─────────────────────────┘                                     └─────────────────────────┘
               │                                                               │
               ▼                                                               ▼
  ┌─────────────────────────┐                                     ┌─────────────────────────┐
  │ Dispatcher & Mainboard  │                                     │  Pulse WebKeeper        │
  │ (Dynamic Router / Sentry)                                     │  (Flask Health Server)  │
  └─────────────────────────┘                                     └─────────────────────────┘
               │                                                               │
       ┌───────┴───────────────┬───────────────────────┐                       │
       ▼                       ▼                       ▼                       ▼
┌──────────────┐       ┌──────────────┐       ┌────────────────┐      ┌─────────────────┐
│ PyMuPDF      │       │ LibreOffice  │       │ Tesseract OCR  │      │ MongoDB Safebox │
│ (44+ PDF Ops)│       │ (Docx/Pptx)  │       │ (ocrmypdf)     │      │ (Motor Async)   │
└──────────────┘       └──────────────┘       └────────────────┘      └─────────────────┘
```

---

## ⚙️ Concurrency & Worker Management

- **Client Driver:** Built on **Kurigram** (an optimized Pyrogram fork) using `TgCrypto` for C-accelerated MTProto encryption and decryption.
- **Worker Pool:** Initialized with `workers=20` and `max_concurrent_transmissions=20` to allow parallel document operations without UI latency.
- **File Workspaces:** Each user/chat is assigned an isolated workspace in `/work/roxybasicneedbot/<chat_id>` that is automatically swept and cleaned upon task completion or `/cancel`.
- **Memory Safeguards:** Monitored via `psutil` in `sentinel/secfilter.py` to prevent Out-Of-Memory (OOM) crashes on large multi-hundred-megabyte files.

---

## 📡 Dual Engine & B2B Bridge Protocol

RoxyBasicNeedBot v2 implements a dual-engine architecture:
1. **Primary MTProto Client:** Handles interactive user chats, inline queries, and massive document transfers directly over Telegram's MTProto protocol.
2. **Secondary aiogram 3 Microservice (`bridge/nexus_aiogram.py`):** Acts as a dedicated B2B relay bridge. Partner bots forward documents via Webhook (`POST /webhook/bridge/<token>`), allowing Roxy to act as a centralized, high-performance document rendering backend.

---

## 🗄️ Database Layer (MongoDB Safebox)

The database layer utilizes **Motor** (async Python driver for MongoDB):

```json
{
  "_id": "ObjectId(...)",
  "id": 123456789,
  "lang": "eng",
  "thumb": "AgACAgIAAxkBAAI...",
  "capt": "Custom caption text with {filename}",
  "fname": true,
  "api": "convertapi_key_optional",
  "beta": false,
  "banned": false
}
```

---

## 🩺 Pulse WebKeeper Keep-Alive

To ensure 24/7 uptime on cloud PaaS providers (Render, Koyeb, Railway) without spin-down:
- An asynchronous **Flask** microservice binds to `0.0.0.0:${PORT:-8080}`.
- Exposes `GET /ping` for external heartbeat monitors (UptimeRobot, BetterStack).
- Integrates self-ping background loops if `RENDER_URL` is set in `config.env`.
