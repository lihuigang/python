import shutil
from urllib.request import urlopen
import requests
import re



def getPagelist(url):
    html = urlopen(url)
    text=html.read().decode('UTF-8')
    print (text)
    urlList=(re.findall(r'<a href="(http://.*\?id=\d*)" title=".*">',text))
    return list(set(urlList))

def getPDFname(url):
    Downhtml = urlopen(url)
    Downtext=Downhtml.read().decode('UTF-8')
    PDFname=re.findall(r'<button data-url="https://www.talkingdata.com/reports/archives/pdf/(.*)">提交并下载此报告</button>',Downtext)[0]+".pdf"
    return PDFname


def getDownUrl(url):
    Downhtml = urlopen(url)
    Downtext = Downhtml.read().decode('UTF-8')
    imgList = (re.findall(r'<button data-url="(https://.*/pdf.*)">提交并下载此报告</button>', Downtext))
    return imgList


def DownFile(url,file):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


getPagelist("http://quiz.talkingdata.com/m/17945488.aspx#")