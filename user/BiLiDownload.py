#!/usr/bin/env python3
import sys
import ssl
import urllib.request


def report(count, blockSize, totalSize):
    '''下载进度显示'''
    downloadedSize = count * blockSize
    percent = int(downloadedSize * 100 / totalSize)
    print(downloadedSize,totalSize,percent)
    sys.stdout.flush()


if __name__ == '__main__':
    # 不加这个的话可能会出现 SSL 验证错误
    ssl._create_default_https_context = ssl._create_unverified_context
    opener = urllib.request.build_opener()
    # 请求头
    opener.addheaders = [
    ('Accept','*/*'),
    ('Accept-Encoding','identity;q=1, *;q=0'),
    ('Accept-Language','zh-CN,zh;q=0.9'),
    ('Connection','keep-alive'),
    ('Host','tx.acgvideo.com'),
    ('Range','bytes=0-'),
    ('Referer','https://www.bilibili.com/video/av16653099/index_60.html'),
    ('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'),
    ]
    urllib.request.install_opener(opener)
    url = 'https://tx.acgvideo.com/70/91/27159170/27159170-1-16.mp4?txTime=1514688573&platform=pc&txSecret=454757871308d3207057be22faca57dd&oi=1929272399&rate=114840&hfb=b99ffc3c5c68f00a33123bb25f882d5b'
    urllib.request.urlretrieve(url, filename='av14543079.mp4', reporthook=report)