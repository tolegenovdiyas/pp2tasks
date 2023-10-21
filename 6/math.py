#1
'''
import math
deg = float(input())
radian = math.radians(deg)
print(radian)
'''
#2
'''
import math

h = float(input())
a = float(input())
b = float(input())
area = 0.5 * (a + b) * h
print(area)
'''
#3
'''
import math

number_of_sides=int(input())
length_of_side = int(input())
area = (number_of_sides * length_of_side**2) / (4 * math.tan(math.pi / number_of_sides))
formatted_area = "{:.0f}".format(area)
print(formatted_area)
'''
#4
'''
a= float(input())
h = float(input())
area = a * h
print(area)
'''