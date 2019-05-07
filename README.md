# Bot-deploy
The script deploys a bot which is reported about the checked works on courses of [DEVMAN.org](https://devman.org)

# How to start
Before start to deploy install requirements:

```bash
pip install -r requirements.txt
```

## Environment variables.

1. dvmn-token
2. telegram-token
3. chat_id

.env example:

```
dvmn_token=Token ca7649f65bada10f03b12a09a957518b080a32d2
telegram_token=123456789:CsAYAQKqoiRwp26LJLKssUjQKl28vdWWRWS
chat_id=123456789
```
## How to get

1. *dvmn-token* get from [Devman API](https://dvmn.org/api/docs/)

2. Then send `/start` and `/newbot` commands to [Telegram\'s BotFather](https://telegram.me/BotFather) to take *telegram-token*.

3. Send `/start` to bot for activate it, because you will not be able to work with a bot without activation.

4. To take *chat_id* send `/start` to telegram bot `@userinfobot`

Launch on Linux(Python 3.5) or Windows as simple

```bash
python bot.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
