#!/usr/bin/env python
# coding=utf-8
# 用于渠道分析小时级数据，增加缺失的小时维度，并将其对应的指标值设为默认值 0

#!/usr/bin/env python
# coding=utf-8
import sys


def get_uniqkey(line):
    key = line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + line[3] + "\t" + line[6] + "\t" + line[7] + "\t" + line[8]
    return key

def get_key(line):
    key = line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + line[3] + "\t" + line[7] + "\t" + line[8]
    return key

def get_dic(line):
    dict={}
    values=['0','0']
    for hour in range(0,24):
        key = line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + line[3] + "\t" + str(hour) + "\t" + line[7]+ "\t" + line[8]
        dict[key]=values
    return dict

def get_value(line):
    value_list=[0,0]
    value_list[0] = line[4]
    value_list[1] = line[5]
    return value_list


key=[]
isfirst=1
for row in sys.stdin:
    line = row.strip().split('\t')
    print line
    if key != get_key(line):
        if isfirst!=1 :
            for key in dic:
                print key+"\t"+"\t".join(dic[key])
        else:
            isfirst=0
        dic=get_dic(line)
        isfirst=0
        key=get_key(line)

    dic[get_uniqkey(line)]=get_value(line)
for key in dic:
    print key + "\t" + "\t".join(dic[key])
