from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
def getApps(num):
    html = urlopen("http://mi.talkingdata.com/allApps.html?page="+num)
    bsObj=BS(html.read().decode('UTF-8'),"lxml")
    nameList = bsObj.findAll("dl",{"class":"l"})
    return nameList
applist=[]

def getReport(num):
    html = urlopen("http://mi.talkingdata.com/reports.html?category=all&tag=all&page="+num)
    bsObj=BS(html.read().decode('UTF-8'),"lxml")
    nameList = bsObj.findAll("dl",{"class":"l"})
    return nameList
try:
    for i in range(1,1000):
        print (i)
        list=getApps(str(i))
        if i >1:
            open("1.txt",'a').write(","+str(list))
        else:
            open("1.txt", 'a').write(str(list))
except Exception:
    print ("over")

try:
    list=open("1.txt",'r').read().split(",")
    i=1
    for line in list:
        print (i,re.findall(r'trans\">(.*)\<',line))
        i+=1
except Exception:
    print ("over")