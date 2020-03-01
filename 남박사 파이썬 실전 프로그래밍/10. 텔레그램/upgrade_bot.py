# 200302 08:00
# upgrade_bot - 날씨, 환율 응답, 컴퓨터 파일 전송 기능 추가하기
# 열심히 공부하자, 패스트캠퍼스 인강, 코드잇, 인프런, 파이썬 중급, 이진석님 장고 강의
# 어려워서 5분 27초 까지만

import telepot

TELEGRAM_TOKEN = "1005159877:AAG-JbJX2OqeTuY7X_EQryzE7Tjq-QPa8vw"

import os
def get_dir_list(dir):
    str_list = ""
    if os.path.exists(dir):
        file_list = os.listdir(dir)
        file_list.sort()
        for f in file_list:
            full_path = os.path.join(dir, f)
            if os.path.isdir(full_path):
                f = "[" + f + "]"
            str_list += f
            str_list += "\n"
    str_list.strip()
    return str_list

def handler(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)

    if content_type == "text":
        str_message = msg['text']
        if str_message[0, 1] == "/":
            args = str_message.split(" ")
            command = args[0]
            del args[0]

            if command == "/dir":


bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)