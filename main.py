#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -*- maxc.cc - 2019-09-18  -*-

import requests
from bs4 import BeautifulSoup
import random
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}

# 获取代理ip的list，用于随机选一个
def get_ip_list():
    ip_list = []
    for line in open("proxies.txt"):
        line = line.rstrip("\n")
        IP_Proxy = line
        ip_list.append(IP_Proxy)
        print('get ip list success')
    return ip_list


# 随机从获取到的IP中选一个生成代理IP
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    prox = {'http': proxy_ip}
    print('get random ip - success')
    return prox


# 刷PV的主程序
def mainpv():
    pvurl = ['https://bbs.moxinwangluo.cn/thread-71-1-1.html',
             'https://bbs.moxinwangluo.cn/thread-71-1-1.html',
             'https://bbs.ichunqiu.com/thread-61007-1-1.html',
             'https://bbs.moxinwangluo.cn/thread-56-1-1.html']
    count = 0
    countUrl = len(pvurl)
    print(proxies)

    # 设置一个随机执行的时间
    randomtime = random.randint(1, 5)
    print(randomtime)

    # 访问次数设置限制
    while count < 11:
        try:  # 正常运行
            for i in range(countUrl):
                response = requests.get(pvurl[i], headers=headers, proxies=proxies, timeout=5)
                if response.status_code == 200:
                    count = count + 1
                    print('当前IP完成 ' + str(count)+'次')
            time.sleep(randomtime)
        except Exception:  # 异常
            print('Failed and Retry')


# 运行程序的顺序
if __name__ == '__main__':
    ip_list = get_ip_list()
    S_num=len(ip_list)
    print("共有："+str(S_num)+"个代理IP")
    a = 0
    b = 99999999  # 循环次数
    while a < b:
        proxies = get_random_ip(ip_list)
        mainpv()
        a += 1
