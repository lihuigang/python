#!/usr/bin/env python
# coding=utf-8

for line in sys.stdin:
    line = line.strip().split('\t')
    try:
        for hour in range(1,25):
            print "\t".join(line)+'\t'+str(hour)
    except Exception,e:
        pass