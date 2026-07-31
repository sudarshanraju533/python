"""
1. welcome message function

write a function named welcome_student().

requirements:
- accept a student's name as an argument.
- return a welcome message.
- call the function using a name entered by the user.
- print the returned message.
"""

"""
def welcome_student(name):
    return f"welcome {name}! start learning python functions."

name = input("enter student name: ").strip()

if name:
    print(welcome_student(name))
else:
    print("invalid name")
"""


"""
2. addition of two numbers

write a function named add_numbers() that accepts two numbers and returns their sum.

requirements:
- read two numbers from the user.
- pass them to the function.
- return the sum from the function.
- print the final result.
"""

"""
def add_numbers(number1, number2):
    return number1 + number2


try:
    first_number = float(input("enter first number: "))
    second_number = float(input("enter second number: "))

    result = add_numbers(first_number, second_number)

    print("sum:", result)

except valueerror:
    print("invalid input")
"""


"""
3. calculator using functions

create four separate functions:
- add()
- subtract()
- multiply()
- divide()

requirements:
- accept two numbers from the user.
- ask the user to select an operation.
- call the appropriate function.
- handle division by zero.
- print the calculated result.
"""

"""
def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        return "cannot divide by zero"
    return number1 / number2


try:
    first_number = float(input("enter first number: "))
    second_number = float(input("enter second number: "))
    operation = input("enter operation: ").lower()

    if operation == "add":
        result = add(first_number, second_number)

    elif operation == "subtract":
        result = subtract(first_number, second_number)

    elif operation == "multiply":
        result = multiply(first_number, second_number)

    elif operation == "divide":
        result = divide(first_number, second_number)

    else:
        result = "invalid operation"

    print("result:", result)

except valueerror:
    print("invalid input")
"""


"""
4. even or odd function

write a function named check_even_odd().

requirements:
- accept one integer.
- return even when the number is even.
- return odd when the number is odd.
- read the number from the user.
- print the returned result.
"""

"""
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


try:
    number = int(input("enter a number: "))

    result = check_even_odd(number)

    print(number, "is", result)

except valueerror:
    print("invalid input")
"""


"""
5. find the largest number

write a function named find_largest() that accepts three numbers.

requirements:
- do not use the built-in max() function.
- compare the numbers using conditional statements.
- return the largest number.
- accept three values from the user.
"""

"""
def find_largest(number1, number2, number3):
    largest = number1

    if number2 > largest:
        largest = number2

    if number3 > largest:
        largest = number3

    return largest


try:
    numbers = input("enter three numbers: ").split()

    number1 = float(numbers[0])
    number2 = float(numbers[1])
    number3 = float(numbers[2])

    print("largest number:", find_largest(number1, number2, number3))

except:
    print("invalid input")
"""

"""
6. calculate the square and cube

write two functions:
- calculate_square(number)
- calculate_cube(number)

requirements:
- read one number from the user.
- pass the same number to both functions.
- return the square and cube separately.
- print both results.
"""

"""
def calculate_square(number):
    return number ** 2


def calculate_cube(number):
    return number ** 3


try:
    number = int(input("enter a number: "))

    print("square:", calculate_square(number))
    print("cube:", calculate_cube(number))

except valueerror:
    print("invalid input")
"""


"""
7. area of a rectangle

write a function named rectangle_area().

requirements:
- accept length and width as parameters.
- return the area.
- validate that both values are positive.
- display an error when either value is zero or negative.

formula:
area = length × width
"""

"""
def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        return "length and width must be positive"

    return length * width


try:
    length = float(input("enter length: "))
    width = float(input("enter width: "))

    result = rectangle_area(length, width)

    print("area of rectangle:", result)

except valueerror:
    print("invalid input")
"""


"""
8. area and circumference of a circle

create two functions:
- circle_area(radius)
- circle_circumference(radius)

requirements:
- accept radius from the user.
- use math.pi.
- return area and circumference separately.
- display both values rounded to two decimal places.
"""

"""
import math


def circle_area(radius):
    return math.pi * radius ** 2


def circle_circumference(radius):
    return 2 * math.pi * radius


try:
    radius = float(input("enter radius: "))

    if radius <= 0:
        print("invalid radius")

    else:
        print("area:", round(circle_area(radius), 2))
        print("circumference:", round(circle_circumference(radius), 2))

except valueerror:
    print("invalid input")
"""


"""
9. student grade calculator

write a function named calculate_grade().

requirements:
- accept student's marks.
- return grade according to rules:
  90-100: a
  80-89: b
  70-79: c
  60-69: d
  below 60: f
- validate marks between 0 and 100.
"""

"""
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "invalid marks"

    if marks >= 90:
        return "a"

    elif marks >= 80:
        return "b"

    elif marks >= 70:
        return "c"

    elif marks >= 60:
        return "d"

    else:
        return "f"


try:
    marks = float(input("enter marks: "))

    print("grade:", calculate_grade(marks))

except valueerror:
    print("invalid input")
"""


"""
10. simple interest calculator

write a function named simple_interest().

requirements:
- accept principal, annual interest rate, and time.
- return calculated simple interest.
- accept all values from the user.
- display the result with two decimal places.

formula:
simple interest = (principal × rate × time) / 100
"""

"""
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


try:
    principal = float(input("principal: "))
    rate = float(input("rate: "))
    time = float(input("time: "))

    result = simple_interest(principal, rate, time)

    print("simple interest:", format(result, ".2f"))

except valueerror:
    print("invalid input")
"""

"""
21. positional arguments

write a function named employee_details().

requirements:
- accept employee name, employee id, department, and salary.
- call the function using positional arguments.
- print all details in formatted manner.
- call the function a second time by changing argument order.
- explain the effect in a comment.
"""

"""
def employee_details(name, employee_id, department, salary):
    print("name:", name)
    print("employee id:", employee_id)
    print("department:", department)
    print("salary:", salary)


employee_details("ravi", 101, "it", 50000)


# changing positional argument order changes the values
# because python assigns values according to position.

employee_details(102, "meena", 60000, "hr")
"""


"""
22. keyword arguments

use the same employee_details() function.

requirements:
- call the function using keyword arguments.
- change the order of keyword arguments.
- verify output remains correct.
"""

"""
def employee_details(name, employee_id, department, salary):
    print("name:", name)
    print("employee id:", employee_id)
    print("department:", department)
    print("salary:", salary)


employee_details(
    name="ravi",
    employee_id=101,
    department="it",
    salary=50000
)


# keyword arguments allow changing order

employee_details(
    salary=60000,
    department="hr",
    name="meena",
    employee_id=102
)
"""


"""
23. default arguments

write a function named create_profile().

requirements:
- accept name, city and country.
- set india as default country.
- call function without country.
- call function with different country.
"""

"""
def create_profile(name, city, country="india"):
    print("name:", name)
    print("city:", city)
    print("country:", country)


create_profile("anil", "bengaluru")

create_profile("john", "new york", "usa")
"""


"""
24. variable-length positional arguments

write a function named calculate_total() using *args.

requirements:
- accept any number of numerical values.
- return total.
- do not use sum().
"""

"""
def calculate_total(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(calculate_total(10, 20, 30))

print(calculate_total(1, 2, 3, 4, 5))

print(calculate_total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
"""


"""
25. variable-length keyword arguments

write a function named display_student() using **kwargs.

requirements:
- accept any number of student attributes.
- print every key and value.
"""

"""
def display_student(**details):

    for key, value in details.items():
        print(key, ":", value)


display_student(
    name="ravi",
    age=20,
    course="python",
    city="chennai",
    qualification="bca"
)


display_student(
    name="anitha",
    age=21,
    course="java"
)
"""


"""
26. combine normal arguments and *args

write a function named student_marks().

requirements:
- first parameter should be student name.
- remaining arguments represent marks.
- calculate total and average.
- return both values.
"""

"""
def student_marks(name, *marks):

    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    return total, average


total, average = student_marks(
    "ravi",
    80,
    75,
    90,
    88
)

print("total:", total)
print("average:", average)
"""


"""
27. combine normal arguments and **kwargs

write a function named product_information().

requirements:
- accept product name as normal argument.
- accept additional details using **kwargs.
- print product name first.
- print remaining details.
"""

"""
def product_information(product_name, **details):

    print("product:", product_name)

    for key, value in details.items():
        print(key, ":", value)


product_information(
    "laptop",
    brand="dell",
    ram="16 gb",
    storage="512 gb",
    price=75000
)
"""


"""
28. positional-only parameters

write a function using positional-only parameters.

requirements:
- define divide_numbers(a, b, /).
- return a / b.
- call correctly using positional arguments.
- add incorrect keyword call in comment.
"""

"""
def divide_numbers(a, b, /):

    return a / b


print(divide_numbers(10, 2))


# incorrect:
# divide_numbers(a=10, b=2)
# this gives error because parameters are positional-only.
"""


"""
29. keyword-only parameters

write a function named create_account().

requirements:
- accept username as normal parameter.
- accept email and is_active as keyword-only parameters.
- set is_active=True by default.
"""

"""
def create_account(username, *, email, is_active=True):

    print("username:", username)
    print("email:", email)
    print("active:", is_active)


create_account(
    "ravi",
    email="ravi@gmail.com"
)


create_account(
    "anitha",
    email="anitha@gmail.com",
    is_active=False
)
"""


"""
30. mixed parameter types

create a function named generate_report().

requirements:
- use positional-only parameters.
- use normal parameters.
- use default parameters.
- use variable positional arguments.
- use keyword-only parameters.
- use variable keyword arguments.
"""

"""
def generate_report(
    report_id,
    /,
    title,
    category="general",
    *items,
    author="unknown",
    **details
):

    print("report id:", report_id)
    print("title:", title)
    print("category:", category)
    print("items:", items)
    print("author:", author)

    for key, value in details.items():
        print(key, ":", value)


generate_report(
    101,
    "python report",
    "programming",
    "functions",
    "lambda",
    author="student",
    year=2026,
    status="complete"
)
"""

"""
31. Return Multiple Values

Write a function named number_statistics().

Requirements:
- Accept a list of numbers.
- Return minimum, maximum, total, and average.
- Use tuple unpacking to store returned values.
"""

"""
def number_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average


numbers = list(map(int, input("enter numbers: ").split()))

if numbers:
    minimum, maximum, total, average = number_statistics(numbers)

    print("minimum:", minimum)
    print("maximum:", maximum)
    print("total:", total)
    print("average:", average)
else:
    print("list is empty")
"""


"""
32. Function Returning a Dictionary

Write a function named analyze_text().

Requirements:
- Accept a string.
- Return a dictionary containing:
  total characters
  total words
  total vowels
  total digits
  total spaces
"""

"""
def analyze_text(text):
    vowels = "aeiouAEIOU"

    result = {
        "total characters": len(text),
        "total words": len(text.split()),
        "total vowels": 0,
        "total digits": 0,
        "total spaces": 0
    }

    for char in text:
        if char in vowels:
            result["total vowels"] += 1
        elif char.isdigit():
            result["total digits"] += 1
        elif char == " ":
            result["total spaces"] += 1

    return result


text = input("enter text: ")

analysis = analyze_text(text)

for key, value in analysis.items():
    print(key, ":", value)
"""


"""
33. Function Returning a List

Write a function named get_even_numbers().

Requirements:
- Accept starting number and ending number.
- Return a list containing even numbers.
- Validate starting number is smaller than ending number.
"""

"""
def get_even_numbers(start, end):
    if start >= end:
        return []

    even_numbers = []

    for number in range(start, end + 1):
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


start = int(input("enter starting number: "))
end = int(input("enter ending number: "))

result = get_even_numbers(start, end)

if result:
    print(result)
else:
    print("invalid range")
"""


"""
34. Prime Number Function

Write a function named is_prime().

Requirements:
- Accept one integer.
- Return True if prime.
- Return False otherwise.
- Print all prime numbers from 1 to 100.
"""

"""
def is_prime(number):
    if number < 2:
        return False

    for value in range(2, number):
        if number % value == 0:
            return False

    return True


for number in range(1, 101):
    if is_prime(number):
        print(number)
"""


"""
35. Fibonacci Function

Write a function named generate_fibonacci().

Requirements:
- Accept number of terms.
- Return Fibonacci series as a list.
- Handle zero and negative values.
- Do not use recursion.
"""

"""
def generate_fibonacci(terms):
    if terms <= 0:
        return []

    series = [0, 1]

    while len(series) < terms:
        series.append(series[-1] + series[-2])

    return series[:terms]


terms = int(input("enter number of terms: "))

print(generate_fibonacci(terms))
"""

"""
36. Lambda Addition

Create a lambda expression that accepts two numbers and returns their sum.

Requirements:
- Accept two numbers from the user.
- Store the lambda expression in a variable.
- Call the lambda and print the result.
- Also write the same logic using a normal function.
"""

"""
def add_numbers(a, b):
    return a + b


addition = lambda a, b: a + b

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

print("lambda result:", addition(number1, number2))
print("normal function result:", add_numbers(number1, number2))
"""


"""
37. Lambda Square and Cube

Create two lambda expressions:
- One to calculate square.
- One to calculate cube.

Requirements:
- Accept one number from the user.
- Print both results.
- Do not define regular functions.
"""

"""
square = lambda number: number ** 2
cube = lambda number: number ** 3

number = int(input("enter number: "))

print("square:", square(number))
print("cube:", cube(number))
"""


"""
38. Lambda Even or Odd

Write a lambda expression that returns Even or Odd.

Requirements:
- Accept an integer.
- Use conditional expression inside lambda.
- Print the result.
"""

"""
check_even_odd = lambda number: "even" if number % 2 == 0 else "odd"

number = int(input("enter number: "))

print(check_even_odd(number))
"""


"""
39. Lambda Maximum of Two Numbers

Create a lambda expression that returns the larger value.

Requirements:
- Do not use max().
- Test positive, negative and equal values.
"""

"""
largest = lambda a, b: a if a > b else b

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

print("largest:", largest(number1, number2))
"""


"""
40. Lambda Maximum of Three Numbers

Create a lambda expression that returns the largest of three numbers.

Requirements:
- Do not use max().
- Use nested conditional expressions.
"""

"""
largest = lambda a, b, c: a if a > b and a > c else (b if b > c else c)

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
number3 = int(input("enter third number: "))

print("largest:", largest(number1, number2, number3))
"""


"""
41. Sort Tuples Using Lambda

Requirements:
- Sort students by marks ascending.
- Sort students by marks descending.
- Use sorted() with lambda.
"""

"""
students = [
    ("Ravi", 82),
    ("Anitha", 95),
    ("Kiran", 76),
    ("Meena", 89)
]

ascending = sorted(students, key=lambda student: student[1])

descending = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("ascending:", ascending)
print("descending:", descending)
"""


"""
42. Sort Dictionaries by Age

Requirements:
- Use lambda expression as sorting key.
- Display youngest first.
- Display oldest first.
"""

"""
students = [
    {"name": "Ravi", "age": 24},
    {"name": "Anu", "age": 21},
    {"name": "Kiran", "age": 27}
]

youngest = sorted(students, key=lambda student: student["age"])

oldest = sorted(
    students,
    key=lambda student: student["age"],
    reverse=True
)

print("youngest:", youngest)
print("oldest:", oldest)
"""


"""
43. Sort Words by Length

Requirements:
- Accept a sentence.
- Split into words.
- Sort using lambda.
- Same length words should be alphabetical.
"""

"""
sentence = input("enter sentence: ")

words = sentence.split()

sorted_words = sorted(
    words,
    key=lambda word: (len(word), word)
)

print(sorted_words)
"""


"""
44. Lambda String Formatter

Requirements:
- Accept first name and last name.
- Remove extra spaces.
- Return title case full name.
"""

"""
format_name = lambda first, last: (
    first.strip() + " " + last.strip()
).title()

first_name = input("enter first name: ")
last_name = input("enter last name: ")

print(format_name(first_name, last_name))
"""


"""
45. Lambda Discount Calculator

Requirements:
- Accept product price and discount percentage.
- Calculate discount amount and final price.
- Validate inputs before calling lambda.
"""

"""
discount_calculator = lambda price, discount: (
    price - (price * discount / 100)
)

price = float(input("enter product price: "))
discount = float(input("enter discount percentage: "))

if price >= 0 and 0 <= discount <= 100:
    discount_amount = price * discount / 100
    final_price = discount_calculator(price, discount)

    print("discount amount:", discount_amount)
    print("final price:", final_price)

else:
    print("invalid input")
"""

"""
46. Square Numbers Using map()

Requirements:
- Accept numbers from the user.
- Use map() with lambda.
- Convert map object into list.
- Print original and squared lists.
"""

"""
numbers = list(map(int, input("enter numbers: ").split()))

squares = list(map(lambda number: number ** 2, numbers))

print("original list:", numbers)
print("squared list:", squares)
"""


"""
47. Cube Numbers Using map()

Requirements:
- Use map().
- Use a normal named function instead of lambda.
- Display original and transformed lists.
"""

"""
def calculate_cube(number):
    return number ** 3


numbers = list(map(int, input("enter numbers: ").split()))

cubes = list(map(calculate_cube, numbers))

print("original list:", numbers)
print("cube list:", cubes)
"""


"""
48. Convert Celsius List to Fahrenheit

Requirements:
- Use map() and lambda.
- Round converted values to two decimal places.
"""

"""
celsius = list(map(float, input("enter celsius values: ").split()))

fahrenheit = list(
    map(lambda value: round((value * 9 / 5) + 32, 2), celsius)
)

print("celsius:", celsius)
print("fahrenheit:", fahrenheit)
"""


"""
49. Convert Strings to Uppercase

Requirements:
- Accept a list of names.
- Remove extra spaces.
- Convert names to uppercase using map().
"""

"""
names = input("enter names: ").split(",")

cleaned_names = list(
    map(lambda name: name.strip().upper(), names)
)

print(cleaned_names)
"""


"""
50. Find Length of Every Word

Requirements:
- Accept a sentence.
- Split into words.
- Use map() to create word and length tuples.
"""

"""
sentence = input("enter sentence: ")

words = sentence.split()

result = list(
    map(lambda word: (word, len(word)), words)
)

print(result)
"""