#!/usr/bin/python
import sys

def calculateFloor(paren_str):
    floor = 0
    first = False
    for i in range(0, len(paren_str)):
        c = paren_str[i]
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1 and first == False:
            print ("Santa first enters basement at position", i+1)
            first = True
    print(floor)


if __name__ == "__main__":
    f = open('input', 'r')
    calculateFloor(f.readline())
