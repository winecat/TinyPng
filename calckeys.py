#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
#import file

key_used_max = 500	#每个key最大使用次数

def get_keys():
    keys = {}
    file = open("keys.conf")
    line = file.readline()
    while line:
        keyInfo = line.rstrip().strip().split(',,,')
        keyDict = {}
        keyDict['key_id'] = keyInfo[0]
        keyDict['key_time'] = keyInfo[1]
        keyDict['key_count'] = keyInfo[2]
        keys[keyInfo[0]] = keyDict
        #print key_dict
        line = file.readline()
    file.close()
    return keys

def write_file(keys):
    file = open("keys.conf", 'w')
    for (k,v) in  keys.items(): 
        file.write(k+","+v['key_time']+','+v['key_count']+"\n")
    file.close()
    
def check_available_key(keys):
    
    
if __name__ == "__main__":
    aa = get_keys()
    ##print aa
    ##write_file(aa)