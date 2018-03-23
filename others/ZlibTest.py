# coding:utf8
import zlib
str=zlib.compress("131,511,22,23,45,000000,0000,0000,000,0,0,0,0,0,0,0,0,222")

open('zlib.txt','w').write(str.replace('\n','000'))
str=open('zlib.txt','r').readline()
print zlib.decompress(str.replace('000','\n'))
