#!/usr/bin/python

import sys

maxSale = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    key, thisSale = data_mapped
    thisSale = float(thisSale)
    maxSale = max(maxSale, thisSale)

print("Maximum sale: " + str(maxSale))