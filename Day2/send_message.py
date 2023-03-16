# -*- coding: utf-8 -*-
# @Project  :APP
# @File     :send_message
# @Date     :2022/3/17 下午6:06
# @Author   :wanhudong
# @Software :PyCharm
import requests
from case.feishureboot.token import get_token
def send_message():
    # url="https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id"
    url = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=email"
    token = get_token()
    print(token)
    headers = {"Authorization": "Bearer " + token,
               "Content-Type": "application/json; charset=utf-8"}
    # data={
    #     "receive_id": "ou_7410d70e934bea88584d5e4c954fb917",
    #     "content":"{\"text\":\"这是一个测试\"}",
    #     # "content": "{\"text\":\"<at user_id=\\\"ou_155184d1e73cbfb8973e5a9e698e74f2\\\">zongyaozhao</at> test content\"}",
    #     "msg_type": "text"
    # }
    data = {
        "receive_id": "wanhudong@deeproute.ai",
        "content": "{\"text\":\"这是一个测试\"}",
        # "content": "{\"text\":\"<at user_id=\\\"ou_155184d1e73cbfb8973e5a9e698e74f2\\\">zongyaozhao</at> test content\"}",
        "msg_type": "text"
    }
    r=requests.post(url,headers=headers,json=data)
    print(r.json())
if __name__ == '__main__':
    send_message()

