import logging
import os
import requests
import telegram
import time
import traceback

def init_logger(handler):
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)  
    return logger

def get_lesson_result(response):
    last_attempt = response["new_attempts"][0]
    lesson_title = last_attempt["lesson_title"]
    lesson_url = dvmn_url + last_attempt["lesson_url"]
    if last_attempt["is_negative"]:
        lesson_pass = "К сожалению, в работе нашлись ошибки"
    else:
        lesson_pass = "Преподавателю все понравилось, можно приступать к следующему уроку!"
    message = "Преподаватель проверил работу: "
    text = "{message} \"{lesson_title}\" {lesson_url} {lesson_pass}".format(
             message=message,
             lesson_title=lesson_title,
             lesson_url=lesson_url,
             lesson_pass=lesson_pass)     
    return text

if __name__ == "__main__":
    
    class MyLogsHandler(logging.Handler):
        def emit(self, record):
            log_entry = self.format(record)  
            bot.send_message(chat_id=chat_id, text=log_entry)   
            
    dvmn_url = "https://dvmn.org"
    longpolling_url = dvmn_url + "/api/long_polling/"
    headers = {
      "Authorization": f'Token {os.environ["dvmn_token"]}'
    }
    long_polling_timeout = 90
    timestamp_parameter = {"timestamp": ""}
    telegram_token = os.environ["telegram_token"]
    chat_id = os.environ["chat_id"]
    try:
        bot = telegram.Bot(token=telegram_token)
        logger = init_logger(MyLogsHandler())
        logger.info("Бот запущен!")
    except Exception:
        logging.exception("Бот не запущен!")
        exit()
    while True:
        try:
            response = requests.get(
                longpolling_url,
                headers=headers,
                timeout=long_polling_timeout,
                params=timestamp_parameter)
            if not response.ok:
                logging.error(response.text)
                logger.error(f"Ответ от сайта: {response.text}")
                time.sleep(30)
                continue
            response = response.json()
            if response["status"] == "timeout":
                timestamp_parameter["timestamp"] = str(response['timestamp_to_request'])
                logging.info("Информации по проверке уроков пока нет")
            elif response["status"] == "found":
                text = get_lesson_result(response)     
                logger.info(text)
                timestamp_parameter = str(response["last_attempt_timestamp"])
        except (KeyError, requests.exceptions.ReadTimeout, requests.ConnectionError):
            pass
        except Exception:
            logger.exception("Бот упал с ошибкой:")   
            time.sleep(30)
