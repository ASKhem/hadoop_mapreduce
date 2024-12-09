#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if len(data) != 6:
        continue
        
    try:
        date, time, store, item, cost, payment = data
        float(cost)
        print("total\t" + cost)
    except ValueError:
        continue