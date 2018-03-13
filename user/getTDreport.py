import shutil
from urllib.request import urlopen
import requests
import re

def getPagelist(num):
    html = urlopen("http://mi.talkingdata.com/reports.html?category=all&tag=all&page=" + str(num))
    text=html.read().decode('UTF-8')
    urlList=(re.findall(r'<a href="(http://.*\?id=\d*)" title=".*">',text))
    return list(set(urlList))

def getPDFname(url):
    Downhtml = urlopen(url)
    Downtext=Downhtml.read().decode('UTF-8')
    PDFname=re.findall(r'<button data-url="https://www.talkingdata.com/reports/archives/pdf/(.*)">提交并下载此报告</button>',Downtext)[0]+".pdf"
    return PDFname


def getDownUrl(url):
    Downhtml = urlopen(url)
    #Downtext = Downhtml.read().decode('UTF-8')
    Downtext = Downhtml.read().decode('utf-8')
    imgList = (re.findall(r'<button data-url="(https://.*/pdf.*)">提交并下载此报告</button>', Downtext))
    return imgList


def DownFile(url,file):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


for i in range(1,40):
    print (i)
    pagelist=getPagelist(i)
    for j in range(0,len(pagelist)-1):
        url= pagelist[j]
        print (url)
        print (getDownUrl(url),getPDFname(url))
        DownFile(getDownUrl(url)[0],getPDFname(url))