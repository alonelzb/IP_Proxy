#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: luozaibo
# date : 2019-10-28 09:50:00
import requests


def proxy_ip():
    # 代理验证信息
    proxyUser = '个人的通行证书'
    proxyPass = '个人的通行密钥'

    # 代理服务器
    proxyHost = 'http-dyn.abuyun.com'
    proxyPort = '9020'

    proxyMeta = f'http://{proxyUser}:{proxyPass}@{proxyHost}:{proxyPort}'
    proxies = {'http': proxyMeta, 'https': proxyMeta}

    return proxy 

if __name__ == '__main__':
    proxy = proxy_ip()
    # 测试地址
    test_url = 'https://httpbin.org/ip'
    headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
            }
    response = requests.get(test_url, proxies=proxies, headers=headers)
    ip = response.text
    print(ip)
