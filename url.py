#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import httplib 
import sys
reload(sys)
print sys.setdefaultencoding('utf-8')
sys.path.insert(0, 'E:\ProgramData\Anaconda2\Lib\site-packages') ## 本地加载 click模块，正常安装不需要这样子配置
import requests, json

def do_url_request(numStr):
    payload = json.dumps({'fullName': 'x' + numStr, 'mail': 'x' + numStr + '@x-mars.cc'}) # 此处将POST的数据定义为一个字典
    print(payload)
    # Headers属性初始化
    headers = {
        'Host': 'tinypng.com',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Referer' : 'https://tinypng.com/developers',
        'Content-Type': 'application/json',
        'Connection' : 'Keep-Alive'
        }
    request_url = 'https://tinypng.com/web/subscription'               # 需要请求的URL地址
    res = requests.post(request_url, data=payload, headers=headers)
    print(res.text)

##闭区间请求
def loop_reqest(start, end):
    tmp = start
    while tmp =< end:
        tmpStr = str(tmp)
        do_url_request(tmpStr)
        tmp = tmp + 1
    print "succeed !!! loop request %d --> %d  end"%(start, end)
    

if __name__ == "__main__":
    loop_reqest(11, 15)
    
