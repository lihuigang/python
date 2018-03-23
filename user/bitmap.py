#!/usr/bin/env python
# coding:utf8


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

    def countone(self,A):
        result = 0
        for num in A:
            while num != 0:
                result += num % 2
                num >>= 1
        return result



if __name__ == '__main__':
    # MAX=879
    # suffle_array=[45,2,78,35,67,90,879,0,340,123,46]
    suffle_array = range(0,111)
    MAX = max(suffle_array)
    result = []
    bitmap = Bitmap(MAX)
    for num in suffle_array:
        bitmap.set(num)
        #print (bitmap.array)
    for i in range(MAX + 1):
        if bitmap.test(i):
            result.append(i)
    C=[]
    for i in range(1,2):
        C.append(bitmap.array)


    #print ('原始数组为:%s') % suffle_array
    #print ('排序后的数组为:%s') % len(result)
    print (bitmap.inter(C))