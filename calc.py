#!/usr/bin/env python3

import sys
import math
from display import display_sphere
from display import display_cylinder
from display import display_cone
from calc_part2 import calc_delta
from math import *

def calc_sphere(argv):
    display_sphere(argv)
    a = ((float(argv[5])) * (float(argv[5]))) + ((float(argv[6])) * (float(argv[6]))) + ((float(argv[7])) * (float(argv[7])))
    b = 2 * (((float(argv[2])) * (float(argv[5]))) + ((float(argv[3])) * (float(argv[6]))) + ((float(argv[4])) * (float(argv[7]))))
    c = (((float(argv[2])) * (float(argv[2]))) + ((float(argv[3])) * (float(argv[3]))) + ((float(argv[4])) * (float(argv[4])))) - ((float(argv[8])) * (float(argv[8])))
    calc_delta(argv, a, b, c)

def calc_cylinder(argv):
    display_cylinder(argv)
    a = float(argv[5]) * float(argv[5]) + float(argv[6]) * float(argv[6])
    b = 2 * (float(argv[2]) * float(argv[5]) + float(argv[3]) * float(argv[6]))
    c = float(argv[2]) * float(argv[2]) + float(argv[3]) * float(argv[3]) - float(argv[8]) * float(argv[8])
    calc_delta(argv, a, b, c)

def calc_cone(argv):
    display_cone(argv)
    angle = math.radians((90 + float(argv[8])) * 2.0)
    tan = math.tan(angle)
    a = float(argv[5])**2 + float(argv[6])**2 - (float(argv[7])**2 / tan**2)
    b = 2 * (float(argv[2]) * float(argv[5]) + float(argv[3]) * float(argv[6]) - ((float(argv[4]) * float(argv[7])) / tan**2))
    c = float(argv[2])**2 + float(argv[3])**2 - (float(argv[4])**2 / tan**2)
    calc_delta(argv, a, b, c)