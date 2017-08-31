# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b,h):
    a = b * h
    return a
def trapezoid_area(b,h):
    a = (a + b)/2 * h
    return a 
# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(parallelogram_area(3,5))



