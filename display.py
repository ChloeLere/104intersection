#!/usr/bin/env python3

import sys
import math

def display_sphere(argv):
    print("Sphere of radius", argv[8])
    print("Line passing through the point ("+str(argv[2])+", "+str(argv[3])+", "+str(argv[4])+") and parallel to the vector ("+str(argv[5])+", "+str(argv[6])+", "+str(argv[7])+")")

def display_cylinder(argv):
    print("Cylinder of radius", argv[8])
    print("Line passing through the point ("+str(argv[2])+", "+str(argv[3])+", "+str(argv[4])+") and parallel to the vector ("+str(argv[5])+", "+str(argv[6])+", "+str(argv[7])+")")

def display_cone(argv):
    print("Cone with a", argv[8],"degree angle")
    print("Line passing through the point ("+str(argv[2])+", "+str(argv[3])+", "+str(argv[4])+") and parallel to the vector ("+str(argv[5])+", "+str(argv[6])+", "+str(argv[7])+")")