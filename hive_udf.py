#!/usr/bin/python

import sys

for line in sys.stdin:
        c_custkey,c_name,c_address,c_city,c_nation,c_region,c_phone,c_mktsegment = line.strip().split('\t')
        c_address= c_address[:6]
        for i in range(len(c_city)):
                if c_city[i].isdigit():
                        city, num = c_city[:i], c_city[i:]
                        break
        c_city = city.strip() + ' #' + num
        print('\t'.join([c_custkey,c_address,c_city]))
