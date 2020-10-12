#!/usr/bin/python

import sys

for line in sys.stdin:
        line = line.strip().split('|')
        lo_quantity, lo_discount, lo_revenue = line[8], line[11], line[12]

        if int(lo_discount) >= 3 and int(lo_discount) <= 5:
                print('{}\t{}'.format(lo_quantity, lo_revenue))
