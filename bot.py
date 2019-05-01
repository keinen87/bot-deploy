import logging
import os
import requests
import telegram
import time
import traceback

class MyLogsHandler(logging.Handler):

    def emit(self, record):
        log_entry = self.format(record)  
        bot.send_message(chat_id=chat_id, text=log_entry)
        
def get_data(url, headers, params=""):
  response = requests.get(url, headers=headers, timeout=30, params=params)
  return response.json()

if __name__ == '__main__':
    dvmn_url = "https://dvmn.org"
    url = dvmn_url + "/api/long_polling/"
    headers = {
      "Authorization": os.environ["dvmn_token"]
    }
    timestamp_parameter = ""
    telegram_token = os.environ["telegram_token"]
    chat_id = "335075762"
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.INFO)
    logger.addHandler(MyLogsHandler())
    try:
      bot = telegram.Bot(token=telegram_token)
      logger.info('Бот запущен!')
    except Exception:
      logging.error('Бот не запущен!')
    while True:
      try:
        response = get_data(url, headers, params=timestamp_parameter)
        lesson_title = response["new_attempts"][0]["lesson_title"]
        lesson_url = dvmn_url + response["new_attempts"][0]["lesson_url"]
        if response["new_attempts"][0]["is_negative"]:
            lesson_pass = 'К сожалению, в работе нашлись ошибки.'
        else:
            lesson_pass = 'Преподавателю все понравилось, можно приступать к следующему уроку!'
        message = "Преподаватель проверил работу: "
        text = "{message} \"{lesson_title}\" {lesson_url} {lesson_pass}".format(
              message=message,
              lesson_title=lesson_title,
              lesson_url=lesson_url,
              lesson_pass=lesson_pass)      
        logger.info(text)
        timestamp_parameter = str(response["last_attempt_timestamp"])
      except requests.exceptions.ReadTimeout:   
        pass
      except Exception:
        logger.info('Бот упал с ошибкой:')   
        logger.info(traceback.format_exc())
        time.sleep(30)      
