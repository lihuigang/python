from urllib.request import urlopen
import sys
import io
from urllib import request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'_lxsdk=1611e090165c8-057cc84ee19058-32637402-1fa400-1611e090165c8; _lxsdk_cuid=1611e0917d7c8-00e36e56e6a9c-32637402-1fa400-1611e0917d8c8; _ga=GA1.2.636300589.1516707187; _gid=GA1.2.1636752255.1516707187; execEngine=presto; statDs=DW_PRESTO_DB_CONNECT_URL; displayName=dw_hiveDW_PRESTO_DB_CONNECT_URL; skmtutc=V4DRtwuTOSZlRNPbWin5JWy3jE/QkOz5XUFCxlSzlffZa362QzloqJOIGl1mafRj-lgvtKOb26DVlBUM/biuDstacLKA=; __mta=50566806.1516711554528.1516799022563.1516799027518.9'

#登录后才能访问的网页
url = 'https://book.sankuai.com/#/'

req = request.Request(url)
resp = request.urlopen(req)
data=resp.getheader('Content-Encoding')
print(data)




req.add_header('cookie',cookie_str)
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
req.add_header('Host','book.sankuai.com')

resp = request.urlopen(req)
#print(resp.read().decode('utf-8'))
#print(resp.read().)