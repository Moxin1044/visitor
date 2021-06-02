import requests
from bs4 import BeautifulSoup
import random
import time

proxiesurl = 'http://www.66ip.cn/mo.php?sxb=&tqsl=2998&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Host': 'www.66ip.cn',
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


print(get_ip_list())
