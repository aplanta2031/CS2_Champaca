import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

point_a = pow(x2-x1,2)
point_b = pow(y2-y1,2)
distance = math.sqrt(point_a+point_b)

print("The distance: ", distance)
