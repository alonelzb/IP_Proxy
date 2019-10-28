#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: luozaibo
# date : 2019-10-28 09:50:00
import requests
import urllib3
import sys
import hashlib
import base64
import time

def proxy_ip():
    # 验证信息
    orderno = 'ZF2018×××××××××××××'
    secret = '5ed83×××××××××××××××'

    ip_port = 'forward.xdaili.cn:80'

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    _version = sys.version_info
    timestamp = str(int(time.time()))
    string = 'orderno=' + orderno + ',' + 'secret=' + secret + ',' + 'timestamp=' + timestamp
    if (_version[0] == 3):
        string = string.encode()

    md5_string = hashlib.md5(string).hexdigest()
    sign = md5_string.upper()
    auth = 'sign=' + sign + '&' + 'orderno=' + orderno + '&' + 'timestamp=' + timestamp

    proxy = {'http': 'http://' + ip_port, 'https': 'https://' + ip_port}
    headers = {'Proxy-Authorization': auth, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

    return proxy, headers


if __name__ == '__main__':
    proxy, headers = proxy_ip()
    test_url = 'https://httpbin.org/ip'
    r = requests.get(test_url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.text)
