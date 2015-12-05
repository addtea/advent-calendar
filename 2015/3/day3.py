#!/usr/bin/python
import sys

def getHouse(x, y, c):
    if c == "^":
        y += 1
    elif c == "v":
        y -= 1
    elif c == ">":
        x += 1
    elif c == "<":
        x -= 1
    return x, y

def calculatePresents(directions):
    # pos = x, y
    x, y = 0,0
    houses = set()
    houses.add((x,y))
    for i in range(0,len(directions)):
        c = directions[i]
        x,y = getHouse(x,y,c)
        houses.add((x,y))
    print (len(houses) ,"houses are given presents")

def calculatePresentsWithRobo(directions):
    xs, ys = 0,0
    xr, yr = 0,0
    houses = set()
    houses.add((xs,ys))
    for i in range(0,len(directions)):
        c = directions[i]
        if (i % 2 == 0):
            xs, ys = getHouse(xs, ys, c)
        else:
            xr, yr = getHouse(xr, yr, c)
        houses.add((xs,ys))
        houses.add((xr,yr))
    print (len(houses), "houses are given presents when working with robo santa")



if __name__ == "__main__":
    f = open('input', 'r')
    directions = f.readline()
    calculatePresents(directions)
    calculatePresentsWithRobo(directions)
