#1. calculate square root of a number using math module

"""
import math

num = float(input("enter a number: "))

print("square root:", math.sqrt(num))
"""


#2. find the cube root of a given number using mathematical operations

"""
num = float(input("enter a number: "))

cube_root = num ** (1 / 3)

print("cube root:", cube_root)
"""


#3. calculate the factorial of a number using math.factorial()

"""
import math

num = int(input("enter a number: "))

print("factorial:", math.factorial(num))
"""


#4. find the gcd of two numbers using math.gcd()

"""
import math

a = int(input("enter first number: "))
b = int(input("enter second number: "))

print("gcd:", math.gcd(a, b))
"""


#5. find the lcm of two numbers using math.lcm()

"""
import math

a = int(input("enter first number: "))
b = int(input("enter second number: "))

print("lcm:", math.lcm(a, b))
"""


#6. calculate the value of 5 raised to the power of 8 using math.pow()

"""
import math

print("answer:", math.pow(5, 8))
"""


#7. find the absolute value of a negative decimal number using math.fabs()

"""
import math

num = float(input("enter a negative decimal number: "))

print("absolute value:", math.fabs(num))
"""


#8. round a floating point number up using math.ceil()

"""
import math

num = float(input("enter a decimal number: "))

print("ceil value:", math.ceil(num))
"""


#9. round a floating point number down using math.floor()

"""
import math

num = float(input("enter a decimal number: "))

print("floor value:", math.floor(num))
"""


#10. round a floating point number to nearest integer using round()

"""
num = float(input("enter a decimal number: "))

print("rounded value:", round(num))
"""

#11. find the remainder of two numbers using math.fmod()

"""
import math

a = float(input("enter first number: "))
b = float(input("enter second number: "))

print("remainder:", math.fmod(a, b))
"""


#12. find the quotient and remainder using divmod()

"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))

quotient, remainder = divmod(a, b)

print("quotient:", quotient)
print("remainder:", remainder)
"""


#13. calculate sine, cosine, and tangent of 45 degrees

"""
import math

angle = 45

radian = math.radians(angle)

print("sine:", math.sin(radian))
print("cosine:", math.cos(radian))
print("tangent:", math.tan(radian))
"""


#14. convert an angle from degrees to radians

"""
import math

degree = float(input("enter angle in degree: "))

radian = math.radians(degree)

print("radian:", radian)
"""


#15. convert an angle from radians to degrees

"""
import math

radian = float(input("enter angle in radian: "))

degree = math.degrees(radian)

print("degree:", degree)
"""


#16. find logarithm base 10 of a number using math.log10()

"""
import math

num = float(input("enter a number: "))

print("log base 10:", math.log10(num))
"""


#17. find natural logarithm of a number using math.log()

"""
import math

num = float(input("enter a number: "))

print("natural log:", math.log(num))
"""


#18. calculate e raised to the power of x using math.exp()

"""
import math

x = float(input("enter value of x: "))

print("answer:", math.exp(x))
"""


#19. find the value of pi and e from math module

"""
import math

print("pi value:", math.pi)
print("e value:", math.e)
"""


#20. find the distance between two points using math.dist()

"""
import math

x1 = float(input("enter x1: "))
y1 = float(input("enter y1: "))

x2 = float(input("enter x2: "))
y2 = float(input("enter y2: "))

point1 = (x1, y1)
point2 = (x2, y2)

print("distance:", math.dist(point1, point2))
"""

#21. calculate the hypotenuse of a right triangle using math.hypot()

"""
import math

a = float(input("enter first side: "))
b = float(input("enter second side: "))

print("hypotenuse:", math.hypot(a, b))
"""


#22. find the combination (ncr) using math.comb()

"""
import math

n = int(input("enter n value: "))
r = int(input("enter r value: "))

print("combination:", math.comb(n, r))
"""


#23. find the permutation (npr) using math.perm()

"""
import math

n = int(input("enter n value: "))
r = int(input("enter r value: "))

print("permutation:", math.perm(n, r))
"""


#24. check whether a number is finite, infinite, or nan

"""
import math

num = float(input("enter a number: "))

if math.isfinite(num):
    print("number is finite")
elif math.isinf(num):
    print("number is infinite")
elif math.isnan(num):
    print("number is nan")
"""


#25. find the product of all numbers in a list using math.prod()

"""
import math

numbers = []

n = int(input("enter number of elements: "))

for i in range(n):
    value = int(input("enter number: "))
    numbers.append(value)

print("product:", math.prod(numbers))
"""


#26. find the sum of square roots of all numbers in a list

"""
import math

numbers = []

n = int(input("enter number of elements: "))

for i in range(n):
    value = int(input("enter number: "))
    numbers.append(value)

total = 0

for num in numbers:
    total += math.sqrt(num)

print("sum of square roots:", total)
"""


#27. find the largest integer less than or equal to the square root of a given number

"""
import math

num = int(input("enter a number: "))

answer = math.floor(math.sqrt(num))

print("answer:", answer)
"""


#28. calculate compound interest using math.pow()

"""
import math

principal = float(input("enter principal amount: "))
rate = float(input("enter rate of interest: "))
time = int(input("enter time in years: "))

amount = principal * math.pow((1 + rate / 100), time)

interest = amount - principal

print("compound interest:", interest)
print("total amount:", amount)
"""


#29. find the area and circumference of a circle using math.pi

"""
import math

radius = float(input("enter radius: "))

area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius

print("area:", area)
print("circumference:", circumference)
"""


#30. create a scientific calculator using math module

"""
import math

print("1. square root")
print("2. factorial")
print("3. logarithm")
print("4. power")
print("5. sine")
print("6. cosine")
print("7. tangent")
print("8. gcd")
print("9. lcm")

choice = int(input("enter your choice: "))

if choice == 1:
    num = float(input("enter number: "))
    print("square root:", math.sqrt(num))

elif choice == 2:
    num = int(input("enter number: "))
    print("factorial:", math.factorial(num))

elif choice == 3:
    num = float(input("enter number: "))
    print("logarithm:", math.log(num))

elif choice == 4:
    a = float(input("enter base: "))
    b = float(input("enter power: "))
    print("answer:", math.pow(a, b))

elif choice == 5:
    angle = float(input("enter angle: "))
    print("sine:", math.sin(math.radians(angle)))

elif choice == 6:
    angle = float(input("enter angle: "))
    print("cosine:", math.cos(math.radians(angle)))

elif choice == 7:
    angle = float(input("enter angle: "))
    print("tangent:", math.tan(math.radians(angle)))

elif choice == 8:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("gcd:", math.gcd(a, b))

elif choice == 9:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("lcm:", math.lcm(a, b))

else:
    print("invalid choice")
"""