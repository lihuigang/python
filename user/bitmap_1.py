#!/usr/bin/env python
# coding:utf8
import zlib
import sys

class Bitmap(object):
    def __init__(self, max):
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return num / 31

    def calcBitIndex(self, num):
        return num % 31

    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def clean(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << byteIndex))

    def test(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return True
        return False


class BitmapCP():
    def merge(self,A):
        B=A[0]
        for i in range(0,len(A[0])):
            for j in range(0,len(A)):
                B[i] = B[i] | A[j][i]
        return B

    def inter(self,A):
        B=A[0]
        for i in range(0,len(A[0])):
            for j in range(0,len(A)):
                B[i] = B[i] & A[j][i]
        return B

    def count(self,A):
        result = 0
        for num in A:
            while num != 0:
                result += num % 2
                num >>= 1
        return result

    def user(self,list):
        result=[]
        MAX=len(list)*31
        bitmap = Bitmap(MAX)
        bitmap.array=list
        for i in range(MAX):
            if bitmap.test(i):
                result.append(i)
        return result

class transform():
    def to_array(self,str):
        array=[]
        for i in str.split(","):
            array.append(int(i))
        return array

    def to_string(self,array):
        bitmap_string=','.join(str(i) for i in array)
        return zlib.compress(bitmap_string,9)

    def to_bitmap(self,array,MAX):
        #MAX=20000000
        bitmap=Bitmap(MAX)
        for i in array:
            bitmap.set(i)
        return bitmap.array

if __name__ == '__main__':
    key="0000"
    array=[]
    A=transform()
    for line in sys.stdin:
        line=line.split("\t")
        if key == "0000":
            key=line[0]
        if key == line[0]:
            array.append(int(line[1]))
        else:
            bitmap_array=A.to_bitmap(array,int(line[2]))
            print key+"\t"+A.to_string(bitmap_array)
            array=[]
            key = line[0]
            array.append(int(line[1]))
    bitmap_array = A.to_bitmap(array,int(line[2]))
    print key + "\t" + A.to_string(bitmap_array)

