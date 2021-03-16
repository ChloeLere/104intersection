#!/usr/bin/env python3

import sys
import math
from math import *

def find_solution(argv, co, delta):
    if delta < 0:
        print("No intersection point.")
        return 0
    if delta == 0:
        res = (-co[1]) / (2 * co[0])
        print("1 intersection point:")
        calc_coord(argv, res)
        return 0
    if delta > 0:
        x1 = (-co[1] + sqrt(delta)) / (2 * co[0])
        x2 = (-co[1] - sqrt(delta)) / (2 * co[0])
        print("2 intersection points:")
        calc_coord(argv, x1)
        calc_coord(argv, x2)
        return 0

def calc_delta(argv, a, b, c):
    delta = ((b) * (b)) - (4 * (a) * (c))
    if a == 0:
        print("There is an infinite number of intersection points.")
        return 0
    co = [a ,b ,c]
    find_solution(argv, co, delta)

def calc_coord(argv, xres):
    x = (float(argv[2])) + ((float(xres)) * (float(argv[5])))
    y = (float(argv[3])) + ((float(xres)) * (float(argv[6])))
    z = (float(argv[4])) + ((float(xres)) * (float(argv[7])))
    print("(%.3f," %x, "%.3f," %y, "%.3f)" %z)