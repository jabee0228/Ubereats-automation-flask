from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import function_list
from main import uber
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('LnjdfCND7wPIAvtFMsqK3hHuIGY1ZAy4OM4r04CUI8E108f+7US7q/M33q393dMm7bIfk5ZKz9YgMEqCGQEhzXX0OcyAgnKvHLCiyfrUYc5sPu8ICR/oK0zXWWuJqzjlndnTNgG6EFEUUPRHywRNQAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('d5bf412afc2e90db887eb0082fb10488')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '姜義新帥嗎' in msg:
        msg = '基本上是帥到無法形容啦！'
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)

        line_bot_api.reply_message(event.reply_token, message)

        message = uber()
        print("outuber")
        print(message)
        line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
