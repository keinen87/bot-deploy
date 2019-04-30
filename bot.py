import os
import requests
import telegram

def get_data(url, headers, params=""):
  response = requests.get(url, headers=headers, timeout=30, params=params)
  return response.json()

if __name__ == '__main__':
    dvmn_url = "https://dvmn.org"
    url = dvmn_url + "/api/long_polling/"
    headers = {
      "Authorization": os.getenv("dvmn_token")
    }
    timestamp_parameter = ""
    telegram_token = os.getenv("telegram_token")
    chat_id = "335075762"
    bot = telegram.Bot(token=telegram_token)
    while True:
      try:
        response = get_data(url, headers, params=timestamp_parameter)
        lesson_title = response["new_attempts"][0]["lesson_title"]
        lesson_url = dvmn_url + response["new_attempts"][0]["lesson_url"]
        message = "Преподаватель проверил работу: "
        text = "{message} \"{lesson_title}\" {lesson_url}".format(
              message=message,
              lesson_title=lesson_title,
              lesson_url=lesson_url)
        bot.send_message(chat_id=chat_id, text=text)
        timestamp_parameter = str(response["last_attempt_timestamp"])
      except requests.exceptions.ReadTimeout:   
        pass
