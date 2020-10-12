#!/usr/bin/python

import sys

prev_quan = None
sum_rev = 0

for line in sys.stdin:
        quan, rev = line.strip().split('\t')
        rev = int(rev)
        if not prev_quan:
                prev_quan = quan
                sum_rev += rev
        elif prev_quan == quan:
                prev_quan = quan
                sum_rev += rev
        else:
                print('{}\t{}'.format(prev_quan, sum_rev))
                prev_quan = quan
                sum_rev = rev
                
print('{}\t{}'.format(prev_quan, sum_rev))
