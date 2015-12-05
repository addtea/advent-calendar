#!/usr/bin/python
import sys
from functools import reduce
import operator

def calculateWrapping(lines):
    total = 0
    for line in lines:
        l,w,h = [int(x) for x in line.split('x')]
        lw=2*l*w
        wh=2*w*h
        hl=2*h*l
        slack=min(l*w,w*h,h*l)
        total += lw+wh+hl+slack
    print(total, "sq ft. of wrapping")

def calculateRibbons(lines):
    total = 0
    for line in lines:
        d = sorted([int(x) for x in line.split('x')])
        ribbon = d[0] * 2 + d[1] * 2
        bow = reduce(operator.mul, d, 1)
        total += ribbon+bow
    print(total, "ft. of ribbon")



if __name__ == "__main__":
    f = open('input', 'r')
    lines = f.read().splitlines()
    calculateWrapping(lines)
    calculateRibbons(lines)
