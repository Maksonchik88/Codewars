"""https://www.codewars.com/kata/5830e7feff1a3ce8d4000062/train/python"""
import math

def ellipse(a, b):
    return f"Area: {round((math.pi*a*b), 1)}, perimeter: {round((math.pi * (3/2*(a+b) - math.sqrt(a*b))), 1)}"

print(ellipse(5, 2), "Area: 31.4, perimeter: 23.1")
print(ellipse(6, 8), "Area: 150.8, perimeter: 44.2")
print(ellipse(13, 1), "Area: 40.8, perimeter: 54.6")