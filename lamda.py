"""
section 1: lambda expressions
question 1
number = 8
write a lambda expression to calculate the square of number.
"""

"""
number=8
square=lambda x:x**2
print(square(number))
"""

"""
question 2
number = 5
write a lambda expression to calculate the cube of number.
"""

"""
number=5
cube=lambda x:x**3
print(cube(number))
"""

"""
question 3
a = 25
b = 17
write a lambda expression to add a and b.
"""

"""
a=25
b=17
add=lambda x,y:x+y
print(add(a,b))
"""

"""
question 4
a = 50
b = 18
write a lambda expression to subtract b from a.
"""

"""
a=50
b=18
subtract=lambda x,y:x-y
print(subtract(a,b))
"""

"""
question 5
a = 12
b = 9
write a lambda expression to multiply a and b.
"""

"""
a=12
b=9
multiply=lambda x,y:x*y
print(multiply(a,b))
"""

"""
question 6
a = 100
b = 4
write a lambda expression to divide a by b.
"""

"""
a=100
b=4
divide=lambda x,y:x/y
print(divide(a,b))
"""

"""
question 7
a = 72
b = 91
write a lambda expression to return the larger number.
"""

"""
a=72
b=91
larger=lambda x,y:x if x>y else y
print(larger(a,b))
"""

"""
question 8
a = 46
b = 28
write a lambda expression to return the smaller number.
"""

"""
a=46
b=28
smaller=lambda x,y:x if x<y else y
print(smaller(a,b))
"""

"""
question 9
number = 34
write a lambda expression that returns true when number is even.
"""

"""
number=34
even=lambda x:x%2==0
print(even(number))
"""

"""
question 10
number = 27
write a lambda expression that returns true when number is odd.
"""

"""
number=27
odd=lambda x:x%2!=0
print(odd(number))
"""

"""
question 11
length = 12
width = 8
calculate area of rectangle using lambda.
"""

"""
length=12
width=8
area=lambda x,y:x*y
print(area(length,width))
"""

"""
question 12
radius = 7
calculate area of circle using 3.14.
"""

"""
radius=7
circle_area=lambda r:3.14*r*r
print(circle_area(radius))
"""

"""
question 13
length = 15
width = 10
calculate perimeter of rectangle.
"""

"""
length=15
width=10
perimeter=lambda x,y:2*(x+y)
print(perimeter(length,width))
"""

"""
question 14
celsius = 35
convert celsius into fahrenheit.
"""

"""
celsius=35
fahrenheit=lambda c:(c*9/5)+32
print(fahrenheit(celsius))
"""

"""
question 15
fahrenheit = 104
convert fahrenheit into celsius.
"""

"""
fahrenheit=104
celsius=lambda f:(f-32)*5/9
print(celsius(fahrenheit))
"""

"""
question 16
word = "python"
return length of string.
"""

"""
word="python"
length=lambda x:len(x)
print(length(word))
"""

"""
question 17
word = "azure"
return first character of string.
"""

"""
word="azure"
first_character=lambda x:x[0]
print(first_character(word))
"""

"""
question 18
word = "databricks"
return last character of string.
"""

"""
word="databricks"
last_character=lambda x:x[-1]
print(last_character(word))
"""

"""
question 19
number = -45
return absolute value without using abs().
"""

"""
number=-45
absolute=lambda x:x if x>=0 else -x
print(absolute(number))
"""

"""
question 20
marks = 72
return distinction, pass or fail.
"""

"""
marks=72
result=lambda x:"distinction" if x>=75 else "pass" if x>=40 else "fail"
print(result(marks))
"""