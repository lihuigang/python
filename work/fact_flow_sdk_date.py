#!/usr/bin/env python
# coding=utf-8

import datetime
import sys
for line in sys.stdin:
    try:
        status='true'
        line=line.strip().split('\t')
        s=line[-2]
        e=line[-1]
        start=s[:4]+'-'+s[4:6]+'-'+s[6:8]
        i=0
        while status=='true':
            dt=datetime.datetime.strptime(start,'%Y-%m-%d')
            dt=dt+datetime.timedelta(days=i)
            dt=datetime.datetime.strftime(dt,'%Y%m%d')
            if dt == e:
                print "\t".join(line[:-2])+'\t'+dt
                status='false'
            else:
                print "\t".join(line[:-2])+'\t'+dt
            i+=1
    except Exception,e:
        pass