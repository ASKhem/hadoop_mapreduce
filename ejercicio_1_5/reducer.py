#!/usr/bin/python

import sys

totalSales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    key, thisSale = data_mapped
    thisSale = float(thisSale)
    totalSales += thisSale

print("Total sales: " + str(totalSales))