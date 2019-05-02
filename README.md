# Bot-deploy
The script deploys a bot which is reported about the checked works on courses of [DEVMAN.org](https://devman.org)

# How to start
Before start to deploy install requirements:

```bash
pip install -r requirements.txt
```
There are environment variables.

1. *dvmn-token* get from [Devman API](https://dvmn.org/api/docs/)

2. Then send `/start` and `/newbot` commands to [Telegram\'s BotFather](https://telegram.me/BotFather). Take *telegram-token* look like `95132391:wP3db3301vnrob33BZdb33KwP3db3F1I`. Send `/start` to bot for activate it.

3. To take *chat_id* send `/start` to telegram bot `@userinfobot`

Launch on Linux(Python 3.5) or Windows as simple

```bash
python bot.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
