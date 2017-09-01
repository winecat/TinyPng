#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'JustFantasy'

import requests, json

payload = json.dumps({'fullName': 'x8', 'mail': 'x8@x-mars.cc'})                              # 此处将POST的数据定义为一个字典
print(payload)
# Headers属性初始化
headers =  {
            'Host': 'tinypng.com',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Referer' : 'https://tinypng.com/developers',
            'Content-Type': 'application/json',
            'Connection' : 'Keep-Alive'
        }
request_url = 'https://tinypng.com/web/subscription'               # 需要请求的URL地址

res = requests.post(request_url, data=payload, headers=headers)
print(res.text)
