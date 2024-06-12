'''Aswad Akram (Assignment #02)
Area Of Circle'''

import math

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

radius = 15

area = calculate_circle_area(15)
print(f"The area of the circle is {area:.2f} square units")

#The area of the circle will be 706.86 square units