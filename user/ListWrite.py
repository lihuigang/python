#TD 行业报告下载
import os
#import PIL
import os
import shutil
from reportlab.pdfgen import canvas
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
from reportlab.lib.pagesizes import A4, landscape
import requests
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context


def getPagelist(num):
    html = urlopen("http://mi.talkingdata.com/reports.html?category=all&tag=all&page=" + str(num))
    text=html.read().decode('UTF-8')
    #print(text)
    urlList=(re.findall(r'<a href="(http://.*\?id=\d*)" title=".*">',text))
    return list(set(urlList))

def getPDFname(url):
    Downhtml = urlopen(url)
    Downtext=Downhtml.read().decode('UTF-8')
    #print (Downtext)
    PDFname=re.findall(r'<button data-url="https://www.talkingdata.com/reports/archives/pdf/(.*)">提交并下载此报告</button>',Downtext)[0]+".pdf"
    return PDFname

def getPDFimgs(url):
    Downhtml = urlopen(url)
    Downtext=Downhtml.read().decode('UTF-8')
    #print (Downtext)
    imgList=(re.findall(r'<p><img src="(.*)" alt="\d*.jpg"></p>',Downtext))
    return imgList
def getDownUrl(url):
    Downhtml = urlopen(url)
    Downtext = Downhtml.read().decode('UTF-8')
    #print (Downtext)
    imgList = (re.findall(r'<button data-url="(https://.*/pdf.*)">提交并下载此报告</button>', Downtext))
    return imgList

def saveAsPDF(imglist,PDFname):
    (w, h) = landscape(A4)
    c = canvas.Canvas(PDFname, pagesize=landscape(A4))
    for img in imglist:
        print(img,PDFname)
        c.drawImage(img, 0, 0, w, h)
        c.showPage()
    c.save()

def saveImg(imgUrlList):
    i=1
    fileList=[]
    for url in imgUrlList:
        file="tmp/"+str(i)+".jpg"
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(file, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        fileList.append(file)
        i+=1
    return fileList

def DownFile(url,file):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open("talkingdata/"+file, 'wb') as f:
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