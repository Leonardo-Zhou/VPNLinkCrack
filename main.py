# -*- coding: utf-8 -*-
"""
@File    : main.py
@Time    : 2022/5/26 13:55
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""

import requests
from USER_AGENT import get_ua
from Crypto.Cipher import AES
import base64
import json
import time
import zmail
import datetime
import yagmail


def decrypt(text, t):
    # 可能需要更改
    path = '/path/120306182525'
    key_list = [
        'ks9KUrbWJj46AftX',
        'ks9KUrbWJj46AftX',
        'ks9KUrbWJj46AftX',
        'awdtif20190619ti'
    ]
    key = key_list[t].encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, key)
    msg = cipher.decrypt(base64.b64decode(text)).decode('utf-8')
    b64_msg = msg.split('://')[-1]
    vmess_info = json.loads(base64.b64decode(b64_msg))
    vmess_info['path'] = path
    b_64_msg = base64.b64encode(json.dumps(vmess_info).encode('utf-8'))
    return 'vmess://' + b_64_msg.decode()


def get_vmess(n):
    headers = get_ua()
    vmess_list = []
    url_list = [
        'https://www.lt71126.xyz:20000/api/evmess',
        'https://www.hd327658.xyz:20000/api/evmess',
        'https://www.09898434.xyz/api/evmess?deviceid=49c95313d64fb7c5unknown&apps=cd9186e318e291300db27867d958eae5',
        'https://www.xfjyqirx.xyz:20000/api/evmess'
    ]

    for i in range(n):
        for url in url_list:
            text = requests.get(url, headers=headers).content.decode()
            print(decrypt(text, url_list.index(url)))
            vmess_list.append(decrypt(text, url_list.index(url)))
        time.sleep(0.2)

    return vmess_list

class mail:
    def __init__(self):
        self.user = 'LeonardoZh0u@163.com'
        self.psw = 'UPQIZNFMBABYIMXO'
        self.receiver = '2974519865@qq.com'
        self.receivers = ['"zhou" <2974519865@qq.com>',
                     'Leonardo Zhou <ytrevorzhou@gmail.com>']

    def post_mail(self, content):
        curr_time = datetime.datetime.now()
        m = yagmail.SMTP(user=self.user, password=self.psw, host='smtp.163.com')
        # contents = [content]
        m.send(
            self.receiver,
            '{}:{}时链接'.format(
                curr_time.hour,
                curr_time.minute),
            contents=content)

    def get_mail(self):
        server = zmail.server(self.user, self.psw)
        m = server.get_latest()

        now = datetime.datetime.now().replace(tzinfo=None)
        if m['from'] in self.receivers and (
                now - m['date'].replace(tzinfo=None)).seconds < 70:
            return 1


def through_mail():
    m = mail()
    while True:
        if m.get_mail():
            v_list = get_vmess(5)
            m.post_mail(v_list)
        time.sleep(60)


def computer():
    get_vmess(6)


if __name__ == '__main__':
    computer()