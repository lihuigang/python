#gzip 网页压缩 解压缩
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from urllib import request, parse
import urllib
from io import StringIO
import io
import gzip


def getPagelist(url,num):
    rst= request.Request(url+num)
    rst.add_header('Accept-encoding', 'gzip,deflate')
    data = request.urlopen(rst)
    encoding = data.getheader('Content-Encoding')
    content = data.read()
    if encoding == 'gzip':
        buf = io.BytesIO(content)
        gf = gzip.GzipFile(fileobj=buf)
        content = gf.read().decode('utf-8')
        return content


browser = webdriver.Chrome()# Get local session of firefox
browser.get("https://www.bilibili.com/video/av1524452/?from=search&seid=4023956215406931579#page=1") # Load page
time.sleep(1) # Let the page load
try:
    #all_links = browser.find_element_by_xpath('/a')
    print (browser.get_network_conditions())
except NoSuchElementException:
    assert 0, "can't find f_red"
browser.close()


getPagelist("https://www.bilibili.com/video/av1524452/?from=search&seid=4023956215406931579#page=","1")


