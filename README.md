# Miko Bot 🤖

A Telegram bot built with [Pyrogram](https://docs.pyrogram.org/) and MongoDB.

## Features

- `/start` — Welcome message with random picture
- `/users` — Owner-only: view total user count
- MongoDB user tracking
- Random start picture from a configurable pool

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/miko-bot.git
cd miko-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy or edit `config.py`, or set the following environment variables:

| Variable        | Description                            |
|-----------------|----------------------------------------|
| `APP_ID`        | Telegram API ID (from my.telegram.org) |
| `API_HASH`      | Telegram API Hash                      |
| `BOT_TOKEN`     | Bot token from @BotFather              |
| `OWNER`         | Your Telegram username                 |
| `OWNER_ID`      | Your Telegram user ID                  |
| `DATABASE_URL`  | MongoDB connection URI                 |
| `DATABASE_NAME` | MongoDB database name                  |
| `START_PIC`     | Space-separated image URLs (optional)  |
| `START_MSG`     | Custom start message (optional)        |

### `START_MSG` placeholders

Use any of these in your `START_MSG`:

- `{first}` — User's first name
- `{last}` — User's last name
- `{username}` — User's @username
- `{mention}` — Mention link
- `{id}` — User ID
- `{bot_name}` — Bot's display name
- `{bot_username}` — Bot's @username

### 4. Run the bot

```bash
python3 miko.py
```

## Deploying on VPS

```bash
# Using screen
screen -S miko
python3 miko.py

# Or using systemd / pm2 as preferred
```

## Adding Plugins

Drop any `.py` file into the `plugins/` folder. It will be auto-loaded on startup.

## Credits

Built by [@Anythingbutnew56](https://t.me/Anythingbutnew56)
