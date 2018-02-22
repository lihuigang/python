# 概率测试(两个人A8点~10点来B9~11点来，A比B早的概率)
import random
a=0
b=0
c=100000
for i in range(1,c):
    A=random.uniform(8,10)
    B=random.uniform(9,11)
    if A < B:
        a+=1
print (a)
print (a/c+1/8)


