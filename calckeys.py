#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import time

key_used_max = 500	#每个key最大使用次数
one_month_second = 2678400 #一个月的秒数

# 读取配置表
def get_keys_conf():
    keys = {}
    file = open("keys.conf")
    line = file.readline()
    while line:
        keyInfo = line.rstrip().strip().split(',')
        keyDict = {}
        keyDict['key_id'] = keyInfo[0]
        keyDict['key_time'] = int(keyInfo[1])
        keyDict['key_count'] = int(keyInfo[2])
        keys[keyInfo[0]] = keyDict
        #print key_dict
        line = file.readline()
    file.close()
    return keys

## 数据更新文件
def write_file(keys):
    file = open("keys.conf", 'w')
    for (k,v) in  keys.items(): 
        file.write(k+","+str(v['key_time'])+','+str(v['key_count'])+"\n")
    file.close()
    
## 检查可用的api key 
def check_available_key(keys):
    defaultKey = 'default-None'
    nowTime = int(time.time())
    min = {}
    for (k,v) in  keys.items():
        keyTime = int(v['key_time'])
        keyCount = int(v['key_count'])
        diff = nowTime - keyTime
        if diff >= one_month_second:
            v['key_count'] = 0
        keyCount = int(v['key_count'])
        if keyCount < 500:
            if 'key_id' in min:
                hasKeyCount = min['key_count']
                if hasKeyCount > keyCount:
                    min = v
            else:
               min = v 
    if 'key_id' in min:
        return min
    else:
        return None
    
## 更新次数
def update_key_count(keyDict):
    keyDict['key_count'] = int(keyDict['key_count']) + 1
    keyDict['key_time'] = int(time.time())
    return keyDict
    
if __name__ == "__main__":
    aa = get_keys_conf()
    rr = check_available_key(aa)
    print rr
    rr = update_key_count(rr)
    aa[rr['key_id']] = rr
    write_file(aa)
    ##print rr
    ##print aa
    ##write_file(aa)