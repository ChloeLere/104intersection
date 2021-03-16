#!/usr/bin/env python3

import sys
import math
from calc import calc_sphere
from calc import calc_cylinder
from calc import calc_cone

def display_h(argv):
    if argv[1][0] == '-' and argv[1][1] == 'h':
        print("USAGE")
        print("\t./104intersection opt xp yp zp xv yv zv p")
        print("DESCRIPTION")
        print("\topt             surface option: 1 for a sphere, 2 for a cylindre, 3 for a cone")
        print("\t(xp, yp, zp)    coordinates of a point by which the light ray passes through")
        print("\t(xv, yv, zv)    coordinates of a vector parallel to the light ray")
        print("\tp               parameter: radius of the sphere, radius of the cylindre, or angles formed by the cone and the Z-axis")
        return 1
    return 0

def error(argv):
    ##if len(argv) == 1:
      ##  sys.stderr.write("Error: not enough argument\n")
        ##return 84
    if len(argv) != 9:
        sys.stderr.write("Error: not enough/too many argument\n")
        return 84
    if ((argv[1][0] < '1' or argv[1][0] > '3') or len(argv[1]) > 1):
        sys.stderr.write("SyntaxError: invalid syntax")
        return 84
    for i in range(1, len(argv)):
        for x in range(0, len(argv[i])):
            if ((argv[i][x] < '0' or argv[i][x] > '9') and argv[i][0] != '-' and argv[i][x] != '.'):
                sys.stderr.write("SyntaxError: invalid syntax")
                return 84
    return 0

def error_part2(argv):
    if (argv[1][0] == '1' or argv[1][0] == '2') and argv[8][0] <= '0':
        sys.stderr.write("Error: bad angle\n")
        return 84
    if argv[1][0] == '3' and argv[8] >= '90':
        sys.stderr.write("Error: bad radius\n")
        return 84
    #if argv[1][0] == '3' and (argv[8][0] < '-90' or argv[8][0] >= '90'):
     #   sys.stderr.write("Error: bad radius\n")
      #  return 84

    #if argv[1][0] == '3' and argv[8] == (math.pi):
     #   sys.stderr.write("Error: bad radius\n")
      #  return 84
    #if argv[1][0] == '3' and argv[8] < '-90':
     #   sys.stderr.write("Error: bad radius\n")
      #  return 84
    

    if argv[5][0] == '0' and argv[6][0] == '0' and argv[7][0] == '0':
        sys.stderr.write("Error: null direction vector\n")
        return 84
    return 0

def main(argv):
    if len(argv) == 1:
        sys.stderr.write("Error: not enough argument\n")
        return 84
    if display_h(argv) == 1:
        return 0
    if error(argv) == 84 or error_part2(argv) == 84:
        return 84
    if argv[1][0] == '1':
        calc_sphere(argv)
        return 0
    if argv[1][0] == '2':
        calc_cylinder(argv)
        return 0
    if argv[1][0] == '3':
        calc_cone(argv)
        return 0
    sys.stderr.write("Error")
    return 84