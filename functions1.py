"""
51. Add Two Lists Using map()

Requirements:
- Add corresponding values of two lists.
- Use map() with two iterables.
- Validate equal length.
"""

"""
list1 = list(map(int, input("enter first list: ").split()))
list2 = list(map(int, input("enter second list: ").split()))

if len(list1) == len(list2):

    result = list(
        map(lambda a, b: a + b, list1, list2)
    )

    print(result)

else:
    print("lists must have same length")
"""


"""
52. Multiply Three Lists

Requirements:
- Multiply corresponding values from three lists.
- Use map() with lambda.
"""

"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [2, 2, 2]

result = list(
    map(lambda a, b, c: a * b * c,
        list1, list2, list3)
)

print(result)
"""


"""
53. Extract Names from Dictionaries

Requirements:
- Use map().
- Extract only employee names.
- Do not use loop or list comprehension.
"""

"""
employees = [
    {"id": 101, "name": "Ravi", "department": "IT"},
    {"id": 102, "name": "Meena", "department": "HR"},
    {"id": 103, "name": "Kiran", "department": "Finance"}
]

names = list(
    map(lambda employee: employee["name"], employees)
)

print(names)
"""


"""
54. Calculate Final Product Prices

Requirements:
- Add 18% tax using map().
- Use zip() for final display.
"""

"""
prices = list(map(float, input("enter prices: ").split()))

final_prices = list(
    map(lambda price: round(price + (price * 18 / 100), 2), prices)
)

for original, final in zip(prices, final_prices):
    print(original, "->", final)
"""


"""
55. Normalize Marks Using map()

Requirements:
- Convert marks into values between 0 and 1.
- Use map() and lambda.
- Round values to two decimals.
"""

"""
marks = list(map(int, input("enter marks: ").split()))

normalized_marks = list(
    map(lambda mark: round(mark / 100, 2), marks)
)

print(normalized_marks)
"""

"""
56. Mask Email Addresses

Requirements:
- Use map().
- Keep first character of username.
- Replace remaining username characters with *.
- Keep domain unchanged.
"""

"""
def mask_email(email):
    username, domain = email.split("@")

    if len(username) <= 1:
        return username + "@" + domain

    return username[0] + "*" * (len(username) - 1) + "@" + domain


emails = input("enter emails: ").split()

masked_emails = list(map(mask_email, emails))

print(masked_emails)
"""


"""
57. Format Phone Numbers

Requirements:
- Use map().
- Validate length and digits.
- Return Invalid for invalid numbers.
"""

"""
def format_phone(number):

    if len(number) == 10 and number.isdigit():
        return number[:3] + "-" + number[3:6] + "-" + number[6:]

    return "Invalid"


numbers = input("enter phone numbers: ").split()

formatted_numbers = list(map(format_phone, numbers))

print(formatted_numbers)
"""


"""
58. Convert Words to Title Case

Requirements:
- Accept multiple names separated by commas.
- Remove extra spaces.
- Convert every name to title case using map().
"""

"""
names = input("enter names: ").split(",")

formatted_names = list(
    map(lambda name: name.strip().title(), names)
)

print(formatted_names)
"""


"""
59. Calculate Employee Bonuses

Requirements:
- Use map().
- Calculate 10% bonus.
- Return salary, bonus and total salary tuples.
"""

"""
salaries = list(map(float, input("enter salaries: ").split()))


def calculate_bonus(salary):
    bonus = salary * 0.10
    total = salary + bonus

    return (
        round(salary, 2),
        round(bonus, 2),
        round(total, 2)
    )


result = list(map(calculate_bonus, salaries))

print(result)
"""


"""
60. Apply Different Operations Using Map

Requirements:
- Generate squares, cubes, doubles and half values.
- Use four separate map() operations.
- Use lambda expressions.
"""

"""
numbers = list(map(float, input("enter numbers: ").split()))

squares = list(map(lambda x: x ** 2, numbers))
cubes = list(map(lambda x: x ** 3, numbers))
doubles = list(map(lambda x: x * 2, numbers))
halves = list(map(lambda x: x / 2, numbers))

print("squares:", squares)
print("cubes:", cubes)
print("doubles:", doubles)
print("halves:", halves)
"""


"""
61. Filter Even Numbers

Requirements:
- Use filter() with lambda.
- Return only even numbers.
"""

"""
numbers = list(map(int, input("enter numbers: ").split()))

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print("original:", numbers)
print("even:", even_numbers)
"""


"""
62. Filter Odd Numbers

Requirements:
- Use filter().
- Use named function instead of lambda.
"""

"""
def is_odd(number):
    return number % 2 != 0


numbers = list(map(int, input("enter numbers: ").split()))

odd_numbers = list(filter(is_odd, numbers))

print(odd_numbers)
"""


"""
63. Filter Positive, Negative and Zero Values

Requirements:
- Use filter().
- Return positive, negative and zero values separately.
"""

"""
numbers = list(map(int, input("enter numbers: ").split()))

positive = list(
    filter(lambda x: x > 0, numbers)
)

negative = list(
    filter(lambda x: x < 0, numbers)
)

zeros = list(
    filter(lambda x: x == 0, numbers)
)

print("positive:", positive)
print("negative:", negative)
print("zeros:", zeros)
"""


"""
64. Filter Numbers Greater Than Average

Requirements:
- Calculate average.
- Use filter() to find values greater than average.
"""

"""
numbers = list(map(int, input("enter numbers: ").split()))

average = sum(numbers) / len(numbers)

greater_numbers = list(
    filter(lambda x: x > average, numbers)
)

print("average:", average)
print("greater numbers:", greater_numbers)
"""


"""
65. Filter Words by Minimum Length

Requirements:
- Accept sentence and minimum length.
- Use filter().
- Remove punctuation where possible.
"""

"""
import string


sentence = input("enter sentence: ")
minimum_length = int(input("enter minimum length: "))


words = [
    word.strip(string.punctuation)
    for word in sentence.split()
]


result = list(
    filter(lambda word: len(word) >= minimum_length, words)
)

print(result)
"""

"""
66. Filter Names Starting with a Vowel

Requirements:
- Use filter().
- Return names beginning with A, E, I, O, U.
- Ignore empty strings.
- Check case-insensitively.
"""

"""
def starts_with_vowel(name):
    vowels = "aeiou"

    name = name.strip()

    if name:
        return name[0].lower() in vowels

    return False


names = input("enter names: ").split(",")

result = list(filter(starts_with_vowel, names))

print(result)
"""


"""
67. Filter Prime Numbers

Requirements:
- Write reusable is_prime() function.
- Pass function to filter().
- Handle values below 2.
"""

"""
def is_prime(number):

    if number < 2:
        return False

    for value in range(2, number):
        if number % value == 0:
            return False

    return True


numbers = list(map(int, input("enter numbers: ").split()))

prime_numbers = list(filter(is_prime, numbers))

print(prime_numbers)
"""


"""
68. Filter Palindrome Words

Requirements:
- Accept sentence.
- Use filter() to find palindrome words.
- Ignore case and punctuation.
"""

"""
import string


def is_palindrome(word):

    cleaned = word.strip(string.punctuation).lower()

    return cleaned == cleaned[::-1]


sentence = input("enter sentence: ")

words = sentence.split()

palindrome_words = list(
    filter(is_palindrome, words)
)

print(palindrome_words)
"""


"""
69. Filter Valid Email Addresses

Requirements:
- Use filter().
- Email should contain:
  one @
  characters before @
  dot after @
"""

"""
def valid_email(email):

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    return username != "" and "." in domain


emails = input("enter emails: ").split()

valid_emails = list(
    filter(valid_email, emails)
)

print(valid_emails)
"""


"""
70. Filter Adults from Records

Requirements:
- Use filter().
- Select people aged 18 or above.
- Do not modify original list.
"""

"""
people = [
    {"name": "Ravi", "age": 24},
    {"name": "Anu", "age": 16},
    {"name": "Kiran", "age": 27}
]


adults = list(
    filter(lambda person: person["age"] >= 18, people)
)


for person in adults:
    print(person)
"""


"""
71. Filter High-Salary Employees

Requirements:
- Ask salary threshold.
- Use filter() to select employees.
- Sort selected employees by salary descending.
"""

"""
employees = [
    {"name": "Ravi", "salary": 60000},
    {"name": "Anu", "salary": 45000},
    {"name": "Kiran", "salary": 80000}
]


threshold = int(input("enter salary threshold: "))


selected = list(
    filter(
        lambda employee: employee["salary"] >= threshold,
        employees
    )
)


selected.sort(
    key=lambda employee: employee["salary"],
    reverse=True
)


print(selected)
"""


"""
72. Filter Products in Stock

Requirements:
- Filter products with stock greater than zero.
- Filter products below budget.
- Filter products satisfying both.
"""

"""
products = [
    {"name": "Laptop", "price": 70000, "stock": 5},
    {"name": "Mouse", "price": 800, "stock": 0},
    {"name": "Keyboard", "price": 1500, "stock": 10}
]


budget = int(input("enter budget: "))


in_stock = list(
    filter(lambda product: product["stock"] > 0, products)
)


below_budget = list(
    filter(lambda product: product["price"] < budget, products)
)


both = list(
    filter(
        lambda product:
        product["stock"] > 0 and product["price"] < budget,
        products
    )
)


print("in stock:", in_stock)
print("below budget:", below_budget)
print("both:", both)
"""


"""
73. Remove Empty Values

Requirements:
- Use filter() without a function.
- Observe truthy and falsy values.
"""

"""
values = [
    "Python",
    "",
    None,
    "Functions",
    0,
    False,
    "Lambda",
    [],
    25
]


# filter() without function removes falsy values.
# Falsy values include empty strings, zero, False, None and empty collections.

result = list(filter(None, values))

print(result)
"""


"""
74. Filter Perfect Squares

Requirements:
- Use filter().
- Write named function.
- Use math module if required.
"""

"""
import math


def is_perfect_square(number):

    if number < 0:
        return False

    root = int(math.sqrt(number))

    return root * root == number


numbers = list(map(int, input("enter numbers: ").split()))


squares = list(
    filter(is_perfect_square, numbers)
)


print(squares)
"""


"""
75. Filter Dates by Year

Requirements:
- Ask user for year.
- Use filter().
- Validate dates using datetime.strptime().
"""

"""
from datetime import datetime


def valid_year(date, year):

    try:
        converted_date = datetime.strptime(
            date,
            "%d-%m-%Y"
        )

        return converted_date.year == year

    except ValueError:
        return False


dates = input("enter dates: ").split()

year = int(input("enter year: "))


result = list(
    filter(
        lambda date: valid_year(date, year),
        dates
    )
)


print(result)
"""

"""
76. Sum Using reduce()

Requirements:
- Import reduce from functools.
- Calculate total using reduce().
- Do not use sum().
- Handle empty list.
"""

"""
from functools import reduce


numbers = list(map(int, input("enter numbers: ").split()))


total = reduce(
    lambda accumulator, value: accumulator + value,
    numbers,
    0
)


print("total:", total)
"""


"""
77. Product Using reduce()

Requirements:
- Use reduce().
- Start with initial value 1.
- Explain accumulator using comments.
"""

"""
from functools import reduce


numbers = list(map(int, input("enter numbers: ").split()))


# accumulator stores the running multiplication result.

product = reduce(
    lambda accumulator, value: accumulator * value,
    numbers,
    1
)


print("product:", product)
"""


"""
78. Maximum Value Using reduce()

Requirements:
- Find largest value using reduce().
- Do not use max().
- Handle empty list.
"""

"""
from functools import reduce


numbers = list(map(int, input("enter numbers: ").split()))


if numbers:

    maximum = reduce(
        lambda a, b: a if a > b else b,
        numbers
    )

    print("maximum:", maximum)

else:
    print("list is empty")
"""


"""
79. Minimum Value Using reduce()

Requirements:
- Find smallest value using reduce().
- Do not use min().
- Test positive and negative values.
"""

"""
from functools import reduce


numbers = list(map(int, input("enter numbers: ").split()))


if numbers:

    minimum = reduce(
        lambda a, b: a if a < b else b,
        numbers
    )

    print("minimum:", minimum)

else:
    print("list is empty")
"""


"""
80. Join Words Using reduce()

Requirements:
- Use reduce() to join words.
- Place one space between words.
- Do not use join().
"""

"""
from functools import reduce


words = input("enter words: ").split()


if words:

    sentence = reduce(
        lambda a, b: a + " " + b,
        words
    )

    print(sentence)

else:
    print("empty list")
"""


"""
81. Calculate Factorial Using reduce()

Requirements:
- Accept non-negative integer.
- Generate numbers from 1 to number.
- Multiply using reduce().
- Reject negative values.
"""

"""
from functools import reduce


def factorial(number):

    if number < 0:
        return None

    numbers = range(1, number + 1)

    return reduce(
        lambda a, b: a * b,
        numbers,
        1
    )


number = int(input("enter number: "))


result = factorial(number)


if result is None:
    print("invalid input")
else:
    print("factorial:", result)
"""


"""
82. Calculate Total Cart Price

Requirements:
- Use map() for item totals.
- Use reduce() for grand total.
"""

"""
from functools import reduce


cart = [
    {"product": "Laptop", "price": 70000, "quantity": 1},
    {"product": "Mouse", "price": 800, "quantity": 2},
    {"product": "Keyboard", "price": 1500, "quantity": 1}
]


item_totals = list(
    map(
        lambda item: item["price"] * item["quantity"],
        cart
    )
)


grand_total = reduce(
    lambda a, b: a + b,
    item_totals,
    0
)


print("item totals:", item_totals)
print("grand total:", grand_total)
"""


"""
83. Find the Longest Word Using reduce()

Requirements:
- Split sentence into words.
- Use reduce().
- Do not use max().
"""

"""
from functools import reduce


sentence = input("enter sentence: ")

words = sentence.split()


if words:

    longest = reduce(
        lambda a, b: a if len(a) >= len(b) else b,
        words
    )

    print("longest word:", longest)

else:
    print("no words")
"""


"""
84. Flatten a Nested List Using reduce()

Requirements:
- Use reduce().
- Create one flat list.
- Do not use nested loops.
"""

"""
from functools import reduce


nested = [
    [1, 2],
    [3, 4],
    [5, 6, 7]
]


flat_list = reduce(
    lambda a, b: a + b,
    nested,
    []
)


print(flat_list)
"""


"""
85. Compose map(), filter() and reduce()

Requirements:
- Use filter() for even numbers.
- Use map() for squares.
- Use reduce() for sum of squares.
"""

"""
from functools import reduce


numbers = list(map(int, input("enter numbers: ").split()))


even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)


squares = list(
    map(lambda x: x ** 2, even_numbers)
)


total = reduce(
    lambda a, b: a + b,
    squares,
    0
)


print("even numbers:", even_numbers)
print("squares:", squares)
print("final total:", total)
"""

"""
86. Basic Nested Function

Requirements:
- Write outer function outer_message().
- Define inner_message() inside it.
- Call inner function from outer function.
"""

"""
def outer_message():

    def inner_message():
        print("this is an inner function message")

    inner_message()


outer_message()
"""


"""
87. Nested Addition Function

Requirements:
- Create calculate().
- Define inner add() function.
- Return addition result.
"""

"""
def calculate(number1, number2):

    def add():
        return number1 + number2

    return add()


first = int(input("enter first number: "))
second = int(input("enter second number: "))


result = calculate(first, second)

print("sum:", result)
"""


"""
88. Three-Level Nested Functions

Requirements:
- Create level_one(), level_two(), level_three().
- Define each function inside previous function.
"""

"""
def level_one():

    print("level one")

    def level_two():

        print("level two")

        def level_three():

            print("level three")

        level_three()

    level_two()


level_one()
"""


"""
89. Closure-Based Multiplier

Requirements:
- Create create_multiplier().
- Return inner multiplier function.
- Create double, triple and ten-times functions.
"""

"""
def create_multiplier(multiplier):

    def multiply(number):
        return number * multiplier

    return multiply


double = create_multiplier(2)
triple = create_multiplier(3)
ten_times = create_multiplier(10)


print(double(10))
print(triple(10))
print(ten_times(10))
"""


"""
90. Closure-Based Discount Calculator

Requirements:
- Create create_discount().
- Return final price after discount.
- Create 10%, 20%, 30% discount functions.
"""

"""
def create_discount(discount):

    def calculate(price):
        return price - (price * discount / 100)

    return calculate


discount_10 = create_discount(10)
discount_20 = create_discount(20)
discount_30 = create_discount(30)


price = float(input("enter price: "))


print("10% discount:", discount_10(price))
print("20% discount:", discount_20(price))
print("30% discount:", discount_30(price))
"""


"""
91. Closure-Based Counter

Requirements:
- Create create_counter().
- Use nonlocal.
- Increase count every call.
"""

"""
def create_counter():

    count = 0

    def counter():

        nonlocal count

        count += 1

        return count

    return counter


counter = create_counter()


print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
"""


"""
92. Closure-Based Bank Balance

Requirements:
- Store balance in outer function.
- Create deposit, withdraw and balance enquiry functions.
- Use nonlocal.
"""

"""
def create_bank_account(balance):

    def deposit(amount):

        nonlocal balance

        balance += amount

        return balance


    def withdraw(amount):

        nonlocal balance

        if amount <= balance:
            balance -= amount
            return balance

        return "insufficient balance"


    def check_balance():

        return balance


    return deposit, withdraw, check_balance


deposit, withdraw, check_balance = create_bank_account(5000)


print(deposit(1000))
print(withdraw(2000))
print(check_balance())
"""


"""
93. Function Decorator

Requirements:
- Create execution_logger().
- Print before and after function execution.
- Preserve return value.
"""

"""
def execution_logger(function):

    def wrapper():

        print("starting function...")

        result = function()

        print("function completed.")

        return result

    return wrapper



@execution_logger
def addition():

    return 10 + 20



print("result:", addition())
"""


"""
94. Local Scope Demonstration

Requirements:
- Create local variable inside function.
- Explain why it cannot be accessed outside.
"""

"""
def show_local():

    message = "local variable"

    print(message)


show_local()


# print(message)
# This gives NameError because message exists only inside the function.
"""


"""
95. Global Scope Demonstration

Requirements:
- Create global variable company.
- Access inside function.
- Create local variable with same name.
"""

"""
company = "Edukron"


def display_company():

    print("global company:", company)



def local_company():

    company = "Python Company"

    print("local company:", company)



print(company)

display_company()

local_company()

print(company)
"""

"""
96. Modify a Global Variable

Requirements:
- Create a global variable named total_students.
- Initially assign value 100.
- Define add_students().
- Use global keyword to update the value.
- Ask the user how many students should be added.
"""

# global variables can be modified inside a function using the global keyword
"""
total_students = 100


def add_students(count):
    global total_students
    total_students += count


print("before adding students:", total_students)

number = int(input("enter number of students to add: "))

if number > 0:
    add_students(number)
    print("after adding students:", total_students)
else:
    print("invalid number")

"""

"""
97. Enclosing Scope Demonstration

Requirements:
- Write an outer function and an inner function.
- Declare message in outer function.
- Access it from inner function.
- Do not pass it as an argument.
"""

"""
def outer_function():
    message = "hello from enclosing scope"

    # inner function can access variables from outer function
    # this is called enclosing scope

    def inner_function():
        print(message)

    inner_function()


outer_function()
"""

"""
98. Modify an Enclosing Variable Using nonlocal

Requirements:
- Write outer_counter().
- Define count = 10.
- Use nonlocal count.
- Increase value by 5.
- Print before and after values.
"""

"""
def outer_counter():
    count = 10

    print("before inner function:", count)

    def inner_function():
        nonlocal count
        count += 5
        print("inside inner function:", count)

    inner_function()

    print("after inner function:", count)


outer_counter()
"""

"""
99. LEGB Name Resolution

Requirements:
- Create variables with the same name at multiple scope levels.
- Use variable name value.
- Demonstrate Local, Enclosing, Global and Built-in scope.

LEGB order:
L - Local
E - Enclosing
G - Global
B - Built-in
"""

value = "global value"

"""
def outer_function():
    value = "enclosing value"

    print("from outer function:", value)

    def inner_function():
        value = "local value"

        print("from inner function:", value)

    inner_function()


print("from global scope:", value)

outer_function()
"""

"""
100. Employee Performance Analysis System

Requirements:
- Use functions.
- Use lambda expressions.
- Use map(), filter(), reduce().
- Use nested functions.
- Use closures.
- Demonstrate LEGB scope.
"""

"""
from functools import reduce


company_name = "Edukron"


employees = [
    {
        "id": 101,
        "name": "Ravi",
        "department": "IT",
        "salary": 60000,
        "performance_score": 88,
        "experience": 5
    },
    {
        "id": 102,
        "name": "Anitha",
        "department": "HR",
        "salary": 45000,
        "performance_score": 72,
        "experience": 4
    },
    {
        "id": 103,
        "name": "Kiran",
        "department": "IT",
        "salary": 75000,
        "performance_score": 94,
        "experience": 7
    },
    {
        "id": 104,
        "name": "Meena",
        "department": "Finance",
        "salary": 55000,
        "performance_score": 81,
        "experience": 6
    },
    {
        "id": 105,
        "name": "Arjun",
        "department": "IT",
        "salary": 40000,
        "performance_score": 65,
        "experience": 2
    }
]


def display_employees():
    for employee in employees:
        print(employee)


def display_names():
    names = list(map(lambda employee: employee["name"], employees))
    print("employee names:", names)


def high_performers():
    result = list(
        filter(lambda employee: employee["performance_score"] >= 80, employees)
    )

    for employee in result:
        print(employee)


def search_department(department):
    result = list(
        filter(
            lambda employee: employee["department"].lower() == department.lower(),
            employees
        )
    )

    if result:
        for employee in result:
            print(employee)
    else:
        print("department not found")


def calculate_revised_salary():
    def increase(employee):
        score = employee["performance_score"]

        if score >= 90:
            increment = 0.15
        elif score >= 80:
            increment = 0.10
        elif score >= 70:
            increment = 0.05
        else:
            increment = 0

        new_employee = employee.copy()
        new_employee["revised_salary"] = (
            employee["salary"] +
            employee["salary"] * increment
        )

        return new_employee

    revised = list(map(increase, employees))

    for employee in revised:
        print(employee)


def salary_expense():

    current_total = reduce(
        lambda x, y: x + y["salary"],
        employees,
        0
    )

    revised_total = reduce(
        lambda x, y: x + y["revised_salary"],
        revised_employees,
        0
    )

    print("current salary:", current_total)
    print("revised salary:", revised_total)
    print("additional expense:", revised_total - current_total)


def highest_paid_employee():

    result = reduce(
        lambda a, b: a if a["salary"] > b["salary"] else b,
        employees
    )

    print(result)


def sort_employees():

    print("sorted by name:")
    print(sorted(employees, key=lambda x: x["name"]))

    print("sorted by salary:")
    print(sorted(employees, key=lambda x: x["salary"]))

    print("sorted by performance:")
    print(sorted(employees, key=lambda x: x["performance_score"]))


def create_bonus_calculator(percent):

    def calculate_bonus(salary):
        return salary * percent / 100

    return calculate_bonus


def generate_department_report(department):

    department_name = department

    selected = list(
        filter(
            lambda employee:
            employee["department"].lower() == department.lower(),
            employees
        )
    )

    def count_employee():
        return len(selected)

    def total_salary():
        return reduce(
            lambda x, y: x + y["salary"],
            selected,
            0
        )

    def average_salary():
        if selected:
            return total_salary() / len(selected)
        return 0

    def average_performance():
        if selected:
            return (
                reduce(
                    lambda x, y: x + y["performance_score"],
                    selected,
                    0
                )
                / len(selected)
            )
        return 0

    report_title = "department report"

    return {
        "company": company_name,
        "title": report_title,
        "department": department_name,
        "employee_count": count_employee(),
        "total_salary": total_salary(),
        "average_salary": average_salary(),
        "average_performance": average_performance()
    }


while True:

    print("\n1. display employees")
    print("2. display names")
    print("3. high performers")
    print("4. search department")
    print("5. revised salaries")
    print("6. highest paid employee")
    print("7. sort employees")
    print("8. department report")
    print("9. exit")

    choice = input("enter choice: ")

    if choice == "1":
        display_employees()

    elif choice == "2":
        display_names()

    elif choice == "3":
        high_performers()

    elif choice == "4":
        department = input("enter department: ")
        search_department(department)

    elif choice == "5":
        calculate_revised_salary()

    elif choice == "6":
        highest_paid_employee()

    elif choice == "7":
        sort_employees()

    elif choice == "8":
        department = input("enter department: ")
        print(generate_department_report(department))

    elif choice == "9":
        print("program ended")
        break

    else:
        print("invalid choice")
"""