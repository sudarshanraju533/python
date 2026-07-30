"""
assignment 1: separate positional and keyword arguments

requirement:

create a function that accepts any number of positional and
keyword arguments.

print:
- number of positional arguments
- number of keyword arguments
- all positional arguments
- all keyword arguments

detailed hints:
- use *args to collect positional arguments.
- use **kwargs to collect keyword arguments.
- args is a tuple.
- kwargs is a dictionary.
- use len() to count values.

def display_arguments(__________, __________):
    positional_count = __________
    keyword_count = __________

    print("positional count:", positional_count)
    print("keyword count:", keyword_count)
    print("positional values:", __________)
    print("keyword values:", __________)

display_arguments(
    10,
    20,
    30,
    name="rahul",
    city="bangalore"
)

expected output:

positional count: 3
keyword count: 2
positional values: (10, 20, 30)
keyword values: {'name': 'rahul', 'city': 'bangalore'}
"""

"""
def display_arguments(*args, **kwargs):
    positional_count = len(args)
    keyword_count = len(kwargs)

    print("positional count:", positional_count)
    print("keyword count:", keyword_count)
    print("positional values:", args)
    print("keyword values:", kwargs)

display_arguments(
    10,
    20,
    30,
    name="rahul",
    city="bangalore"
)
"""


"""
assignment 2: sum only numeric positional arguments

requirement:

accept multiple positional arguments.

add only integer and float values.

ignore strings, lists and other data types.

detailed hints:
- start total with 0.
- loop through args.
- use isinstance(value, (int, float)).
- add the value only when it is numeric.

def calculate_numeric_total(__________):
    total = __________

    for value in __________:
        if isinstance(value, __________):
            total = __________

    return __________

result = calculate_numeric_total(
    10,
    "python",
    20.5,
    [1, 2],
    30
)

print("numeric total:", result)

expected output:

numeric total: 60.5
"""

"""
def calculate_numeric_total(*args):
    total = 0

    for value in args:
        if isinstance(value, (int, float)):
            total = total + value

    return total

result = calculate_numeric_total(
    10,
    "python",
    20.5,
    [1, 2],
    30
)

print("numeric total:", result)
"""


"""
assignment 3: find largest and smallest number

requirement:

accept multiple numbers using *args.

return both the largest and smallest values.

detailed hints:
- check whether args is empty.
- use max() to find the largest number.
- use min() to find the smallest number.
- return two values separated by a comma.

def find_min_max(__________):
    if len(numbers) == __________:
        return None, None

    largest = __________
    smallest = __________

    return __________, __________

maximum, minimum = find_min_max(
    50,
    10,
    80,
    25,
    5
)

print("maximum:", maximum)
print("minimum:", minimum)

expected output:

maximum: 80
minimum: 5
"""

"""
def find_min_max(*numbers):
    if len(numbers) == 0:
        return None, None

    largest = max(numbers)
    smallest = min(numbers)

    return largest, smallest

maximum, minimum = find_min_max(
    50,
    10,
    80,
    25,
    5
)

print("maximum:", maximum)
print("minimum:", minimum)
"""


"""
assignment 4: student marks report

requirement:

accept the student name as a normal argument.

accept marks using *args.

accept extra details using **kwargs.

calculate:
- total marks
- average marks
- pass or fail

passing rule:

the student passes only when every mark is at least 35.

detailed hints:
- use sum(marks) for the total.
- use len(marks) to count subjects.
- use total / len(marks) for average.
- use all(mark >= 35 for mark in marks).
- use kwargs.get() to safely read course and city.

def student_report(name, __________, __________):
    total = __________
    average = __________

    passed = all(mark >= __________ for mark in marks)

    print("student:", name)
    print("course:", kwargs.get("course", "not provided"))
    print("city:", kwargs.get("city", "not provided"))
    print("total:", total)
    print("average:", average)

    if __________:
        print("result: pass")
    else:
        print("result: fail")

student_report(
    "anil",
    80,
    75,
    90,
    65,
    course="python",
    city="hyderabad"
)

expected output:

student: anil
course: python
city: hyderabad
total: 310
average: 77.5
result: pass
"""

"""
def student_report(name, *marks, **kwargs):
    total = sum(marks)
    average = total / len(marks)

    passed = all(mark >= 35 for mark in marks)

    print("student:", name)
    print("course:", kwargs.get("course", "not provided"))
    print("city:", kwargs.get("city", "not provided"))
    print("total:", total)
    print("average:", average)

    if passed:
        print("result: pass")
    else:
        print("result: fail")

student_report(
    "anil",
    80,
    75,
    90,
    65,
    course="python",
    city="hyderabad"
)
"""


"""
assignment 5: employee salary calculator

requirement:

accept:
- employee name as a normal argument
- basic salary as a normal argument
- allowances using *args
- bonuses and other details using **kwargs

calculate:

gross salary = basic salary + allowances + bonus

tax amount = gross salary * tax percentage / 100

net salary = gross salary - tax amount

detailed hints:
- use sum(allowances).
- read bonus using kwargs.get("bonus", 0).
- read tax using kwargs.get("tax", 10).
- do not add every kwargs value because some values may be strings.

def calculate_salary(name, basic_salary, __________, __________):
    allowance_total = __________
    bonus = kwargs.get("bonus", __________)
    tax_percentage = kwargs.get("tax", __________)

    gross_salary = __________ + __________ + __________
    tax_amount = gross_salary * __________ / 100
    net_salary = __________ - __________

    print("employee:", name)
    print("gross salary:", gross_salary)
    print("tax amount:", tax_amount)
    print("net salary:", net_salary)

calculate_salary(
    "rahul",
    50000,
    5000,
    3000,
    2000,
    bonus=10000,
    tax=10,
    department="it"
)

expected output:

employee: rahul
gross salary: 70000
tax amount: 7000.0
net salary: 63000.0
"""

"""
def calculate_salary(name, basic_salary, *allowances, **kwargs):
    allowance_total = sum(allowances)
    bonus = kwargs.get("bonus", 0)
    tax_percentage = kwargs.get("tax", 10)

    gross_salary = basic_salary + allowance_total + bonus
    tax_amount = gross_salary * tax_percentage / 100
    net_salary = gross_salary - tax_amount

    print("employee:", name)
    print("gross salary:", gross_salary)
    print("tax amount:", tax_amount)
    print("net salary:", net_salary)

calculate_salary(
    "rahul",
    50000,
    5000,
    3000,
    2000,
    bonus=10000,
    tax=10,
    department="it"
)
"""

"""
assignment 6: count data types in *args

requirement:

accept multiple positional arguments.

count how many values are:
- integers
- strings
- lists
- other data types

detailed hints:
- create four counters with value 0.
- loop through args.
- use isinstance().
- check bool carefully because bool is a subclass of int.
- you may check type(value) is int for exact integer checking.

def count_data_types(__________):
    integer_count = __________
    string_count = __________
    list_count = __________
    other_count = __________

    for value in values:
        if type(value) is __________:
            integer_count += 1
        elif isinstance(value, __________):
            string_count += 1
        elif isinstance(value, __________):
            list_count += 1
        else:
            other_count += 1

    print("integers:", integer_count)
    print("strings:", string_count)
    print("lists:", list_count)
    print("others:", other_count)

count_data_types(
    10,
    "python",
    [1, 2],
    20,
    "sql",
    3.5,
    True
)

expected output:

integers: 2
strings: 2
lists: 1
others: 2
"""

"""
def count_data_types(*values):
    integer_count = 0
    string_count = 0
    list_count = 0
    other_count = 0

    for value in values:
        if type(value) is int:
            integer_count += 1
        elif isinstance(value, str):
            string_count += 1
        elif isinstance(value, list):
            list_count += 1
        else:
            other_count += 1

    print("integers:", integer_count)
    print("strings:", string_count)
    print("lists:", list_count)
    print("others:", other_count)

count_data_types(
    10,
    "python",
    [1, 2],
    20,
    "sql",
    3.5,
    True
)
"""


"""
assignment 7: filter even and odd numbers

requirement:

accept multiple numbers using *args.

store even numbers in one list.

store odd numbers in another list.

detailed hints:
- create two empty lists.
- use number % 2 == 0 to check even numbers.
- use append() to store values.
- return both lists.

def separate_even_odd(__________):
    even_numbers = __________
    odd_numbers = __________

    for number in numbers:
        if number % 2 == __________:
            __________.append(number)
        else:
            __________.append(number)

    return __________, __________

evens, odds = separate_even_odd(
    10,
    15,
    22,
    31,
    40,
    47
)

print("even numbers:", evens)
print("odd numbers:", odds)

expected output:

even numbers: [10, 22, 40]
odd numbers: [15, 31, 47]
"""

"""
def separate_even_odd(*numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers

evens, odds = separate_even_odd(
    10,
    15,
    22,
    31,
    40,
    47
)

print("even numbers:", evens)
print("odd numbers:", odds)
"""


"""
assignment 8: search employee records

requirement:

create employee records as dictionaries.

accept records using *args.

accept search conditions using **kwargs.

return employees that match every filter.

detailed hints:
- each item in args is one employee dictionary.
- loop through every employee.
- use all() to verify all filters.
- employee.get(key) should equal the expected value.
- add matching employees to a result list.

def search_employees(__________, __________):
    matched_employees = __________

    for employee in employees:
        matches = all(
            employee.get(key) == value
            for key, value in __________.items()
        )

        if __________:
            matched_employees.append(__________)

    return __________

employee1 = {
    "name": "rahul",
    "department": "it",
    "city": "bangalore"
}

employee2 = {
    "name": "anil",
    "department": "hr",
    "city": "hyderabad"
}

employee3 = {
    "name": "priya",
    "department": "it",
    "city": "bangalore"
}

results = search_employees(
    employee1,
    employee2,
    employee3,
    department="it",
    city="bangalore"
)

print(results)

expected output:

[
    {'name': 'rahul', 'department': 'it', 'city': 'bangalore'},
    {'name': 'priya', 'department': 'it', 'city': 'bangalore'}
]
"""

"""
def search_employees(*employees, **kwargs):
    matched_employees = []

    for employee in employees:
        matches = all(
            employee.get(key) == value
            for key, value in kwargs.items()
        )

        if matches:
            matched_employees.append(employee)

    return matched_employees

employee1 = {
    "name": "rahul",
    "department": "it",
    "city": "bangalore"
}

employee2 = {
    "name": "anil",
    "department": "hr",
    "city": "hyderabad"
}

employee3 = {
    "name": "priya",
    "department": "it",
    "city": "bangalore"
}

results = search_employees(
    employee1,
    employee2,
    employee3,
    department="it",
    city="bangalore"
)

print(results)
"""


"""
assignment 9: shopping cart total

requirement:

accept product prices using *args.

accept discount, tax and customer information using **kwargs.

calculate:

subtotal = sum of prices

discount amount = subtotal * discount / 100

amount after discount = subtotal - discount amount

tax amount = amount after discount * tax / 100

final amount = amount after discount + tax amount

detailed hints:
- use kwargs.get("discount", 0).
- use kwargs.get("tax", 0).
- use round(value, 2) while printing.

def checkout(__________, __________):
    subtotal = __________

    discount_percentage = kwargs.get("discount", __________)
    tax_percentage = kwargs.get("tax", __________)

    discount_amount = subtotal * __________ / 100
    discounted_amount = __________ - __________

    tax_amount = discounted_amount * __________ / 100
    final_amount = __________ + __________

    print("customer:", kwargs.get("customer", "guest"))
    print("subtotal:", round(subtotal, 2))
    print("discount:", round(discount_amount, 2))
    print("tax:", round(tax_amount, 2))
    print("final amount:", round(final_amount, 2))

checkout(
    1000,
    500,
    250,
    customer="rahul",
    discount=10,
    tax=18
)

expected output:

customer: rahul
subtotal: 1750
discount: 175.0
tax: 283.5
final amount: 1858.5
"""

"""
def checkout(*prices, **kwargs):
    subtotal = sum(prices)

    discount_percentage = kwargs.get("discount", 0)
    tax_percentage = kwargs.get("tax", 0)

    discount_amount = subtotal * discount_percentage / 100
    discounted_amount = subtotal - discount_amount

    tax_amount = discounted_amount * tax_percentage / 100
    final_amount = discounted_amount + tax_amount

    print("customer:", kwargs.get("customer", "guest"))
    print("subtotal:", round(subtotal, 2))
    print("discount:", round(discount_amount, 2))
    print("tax:", round(tax_amount, 2))
    print("final amount:", round(final_amount, 2))

checkout(
    1000,
    500,
    250,
    customer="rahul",
    discount=10,
    tax=18
)
"""

"""
assignment 10: dynamic configuration manager

requirement:

start with default application settings.

override default values using **kwargs.

return the final configuration.

detailed hints:
- create a default dictionary.
- use dictionary.update().
- kwargs contains the new configuration values.
- return the updated dictionary.

def create_configuration(__________):
    configuration = {
        "host": "localhost",
        "port": 8080,
        "debug": False,
        "timeout": 30
    }

    configuration.__________(kwargs)

    return __________

app_config = create_configuration(
    port=5000,
    debug=True,
    environment="production"
)

print(app_config)

expected output:

{
    'host': 'localhost',
    'port': 5000,
    'debug': True,
    'timeout': 30,
    'environment': 'production'
}
"""

"""
def create_configuration(**kwargs):
    configuration = {
        "host": "localhost",
        "port": 8080,
        "debug": False,
        "timeout": 30
    }

    configuration.update(kwargs)

    return configuration

app_config = create_configuration(
    port=5000,
    debug=True,
    environment="production"
)

print(app_config)
"""


"""
assignment 11: validate required keyword arguments

requirement:

create a registration function.

the following fields are mandatory:
- name
- email
- password

print missing fields when they are not supplied.

detailed hints:
- store required field names in a list.
- use a list comprehension.
- a field is missing when it is not in kwargs.
- if the missing list is empty, registration is successful.

def register_user(__________):
    required_fields = [
        "name",
        "email",
        "password"
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in __________
    ]

    if __________:
        print("missing fields:", missing_fields)
        return False

    print("registration successful")
    return __________

register_user(
    name="rahul",
    email="rahul@example.com"
)

expected output:

missing fields:
['password']
"""

"""
def register_user(**kwargs):
    required_fields = [
        "name",
        "email",
        "password"
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in kwargs
    ]

    if missing_fields:
        print("missing fields:", missing_fields)
        return False

    print("registration successful")
    return True

register_user(
    name="rahul",
    email="rahul@example.com"
)
"""


"""
assignment 12: create a dynamic sql select query

requirement:

accept:
- table name as a normal argument
- column names using *args
- filter conditions using **kwargs

example result:

select name, salary from employee
where department='it' and city='bangalore'

detailed hints:
- use ", ".join(columns).
- if no columns are supplied, use "*".
- build each condition in a list.
- join conditions with " and ".

note:

this is only a string-building exercise.

in a real application, use parameterized sql queries.

def build_select_query(table, __________, __________):
    selected_columns = ", ".join(columns) if columns else __________

    query = f"select {selected_columns} from {__________}"

    if filters:
        conditions = []

        for key, value in filters.items():
            conditions.append(f"{key}='{__________}'")

        query += " where " + " and ".join(__________)

    return __________

query = build_select_query(
    "employee",
    "name",
    "salary",
    department="it",
    city="bangalore"
)

print(query)

expected output:

select name, salary from employee where department='it' and city='bangalore'
"""

"""
def build_select_query(table, *columns, **filters):
    selected_columns = ", ".join(columns) if columns else "*"

    query = f"select {selected_columns} from {table}"

    if filters:
        conditions = []

        for key, value in filters.items():
            conditions.append(f"{key}='{value}'")

        query += " where " + " and ".join(conditions)

    return query

query = build_select_query(
    "employee",
    "name",
    "salary",
    department="it",
    city="bangalore"
)

print(query)
"""


"""
assignment 13: function forwarding with *args and **kwargs

requirement:

create a wrapper function that accepts any arguments.

print the received arguments.

forward those arguments to another function.

detailed hints:
- the wrapper receives *args and **kwargs.
- call the original function using func(*args, **kwargs).
- return the result produced by the original function.

def execute_function(func, __________, __________):
    print("positional arguments:", args)
    print("keyword arguments:", kwargs)

    result = func(__________, __________)

    return __________

def create_employee(
    name,
    age,
    department="it",
    city="bangalore"
):
    return {
        "name": name,
        "age": age,
        "department": department,
        "city": city
    }

employee = execute_function(
    create_employee,
    "rahul",
    28,
    department="data engineering",
    city="hyderabad"
)

print(employee)

expected output:

positional arguments:
('rahul', 28)

keyword arguments:
{'department': 'data engineering', 'city': 'hyderabad'}

{'name': 'rahul', 'age': 28, 'department': 'data engineering', 'city': 'hyderabad'}
"""

"""
def execute_function(func, *args, **kwargs):
    print("positional arguments:", args)
    print("keyword arguments:", kwargs)

    result = func(*args, **kwargs)

    return result

def create_employee(
    name,
    age,
    department="it",
    city="bangalore"
):
    return {
        "name": name,
        "age": age,
        "department": department,
        "city": city
    }

employee = execute_function(
    create_employee,
    "rahul",
    28,
    department="data engineering",
    city="hyderabad"
)

print(employee)
"""


"""
assignment 14: decorator with *args and **kwargs

requirement:

create a decorator that:
- prints the function name
- prints positional arguments
- prints keyword arguments
- executes the original function
- prints the returned result

detailed hints:
- the decorator accepts func.
- the wrapper accepts *args and **kwargs.
- use func.__name__ to get the function name.
- call func(*args, **kwargs).
- return the result.

def log_function_call(func):

    def wrapper(__________, __________):
        print("function name:", __________)
        print("positional:", args)
        print("keyword:", kwargs)

        result = func(__________, __________)

        print("result:", result)

        return __________

    return __________

@log_function_call
def calculate_bill(
    price,
    quantity,
    discount=0
):
    total = price * quantity
    discount_amount = total * discount / 100
    return total - discount_amount

calculate_bill(
    500,
    3,
    discount=10
)

expected output:

function name: calculate_bill
positional: (500, 3)
keyword: {'discount': 10}
result: 1350.0
"""

"""
def log_function_call(func):

    def wrapper(*args, **kwargs):
        print("function name:", func.__name__)
        print("positional:", args)
        print("keyword:", kwargs)

        result = func(*args, **kwargs)

        print("result:", result)

        return result

    return wrapper

@log_function_call
def calculate_bill(
    price,
    quantity,
    discount=0
):
    total = price * quantity
    discount_amount = total * discount / 100
    return total - discount_amount

calculate_bill(
    500,
    3,
    discount=10
)
"""


"""
assignment 15: group numbers based on conditions

requirement:

accept multiple numbers using *args.

accept lower_limit and upper_limit using **kwargs.

divide numbers into:
- below lower limit
- within range
- above upper limit

detailed hints:
- read limits using kwargs.get().
- use three empty lists.
- check lower limit first.
- check upper limit second.
- otherwise, the number is within the range.

def classify_numbers(__________, __________):
    lower_limit = kwargs.get("lower_limit", __________)
    upper_limit = kwargs.get("upper_limit", __________)

    below = []
    within = []
    above = []

    for number in numbers:
        if number < __________:
            below.append(number)
        elif number > __________:
            above.append(number)
        else:
            within.append(number)

    return {
        "below": __________,
        "within": __________,
        "above": __________
    }

classification = classify_numbers(
    5,
    15,
    25,
    35,
    45,
    lower_limit=20,
    upper_limit=40
)

print(classification)

expected output:

{
    'below': [5, 15],
    'within': [25, 35],
    'above': [45]
}
"""

"""
def classify_numbers(*numbers, **kwargs):
    lower_limit = kwargs.get("lower_limit", 0)
    upper_limit = kwargs.get("upper_limit", 100)

    below = []
    within = []
    above = []

    for number in numbers:
        if number < lower_limit:
            below.append(number)
        elif number > upper_limit:
            above.append(number)
        else:
            within.append(number)

    return {
        "below": below,
        "within": within,
        "above": above
    }

classification = classify_numbers(
    5,
    15,
    25,
    35,
    45,
    lower_limit=20,
    upper_limit=40
)

print(classification)
"""

"""
assignment 16: merge multiple dictionaries

requirement:

accept multiple dictionaries using *args.

accept final override values using **kwargs.

merge all dictionaries into one dictionary.

later values should replace earlier values.

detailed hints:
- start with an empty result dictionary.
- loop through args.
- use update() for every dictionary.
- finally update the result with kwargs.

def merge_dictionaries(__________, __________):
    merged = __________

    for dictionary in dictionaries:
        if isinstance(dictionary, __________):
            merged.__________(dictionary)

    merged.__________(overrides)

    return __________

result = merge_dictionaries(
    {"name": "rahul", "city": "bangalore"},
    {"department": "it", "experience": 3},
    {"experience": 4},
    city="hyderabad",
    salary=80000
)

print(result)

expected output:

{
    'name': 'rahul',
    'city': 'hyderabad',
    'department': 'it',
    'experience': 4,
    'salary': 80000
}
"""

"""
def merge_dictionaries(*dictionaries, **overrides):
    merged = {}

    for dictionary in dictionaries:
        if isinstance(dictionary, dict):
            merged.update(dictionary)

    merged.update(overrides)

    return merged

result = merge_dictionaries(
    {"name": "rahul", "city": "bangalore"},
    {"department": "it", "experience": 3},
    {"experience": 4},
    city="hyderabad",
    salary=80000
)

print(result)
"""


"""
assignment 17: etl pipeline summary

requirement:

accept:
- source and destination as normal arguments
- table names using *args
- pipeline options using **kwargs

calculate:
- number of tables
- total estimated rows
- number of batches

number of batches:
total_rows divided by batch_size, rounded upward.

detailed hints:
- read row_counts from kwargs.
- row_counts should be a dictionary.
- use sum(row_counts.get(table, 0) for table in tables).
- use math.ceil() for upward rounding.
- import math before using math.ceil().

import math

def etl_summary(source, destination, __________, __________):
    row_counts = kwargs.get("row_counts", {})
    batch_size = kwargs.get("batch_size", __________)

    table_count = __________

    total_rows = sum(
        row_counts.get(table, 0)
        for table in __________
    )

    batches = math.ceil(__________ / __________) if total_rows else 0

    print("source:", source)
    print("destination:", destination)
    print("tables:", tables)
    print("table count:", table_count)
    print("total rows:", total_rows)
    print("required batches:", batches)

etl_summary(
    "sql server",
    "adls gen2",
    "customer",
    "orders",
    "products",
    row_counts={
        "customer": 12000,
        "orders": 55000,
        "products": 3000
    },
    batch_size=10000
)

expected output:

source: sql server
destination: adls gen2
tables: ('customer', 'orders', 'products')
table count: 3
total rows: 70000
required batches: 7
"""

"""
import math

def etl_summary(source, destination, *tables, **kwargs):
    row_counts = kwargs.get("row_counts", {})
    batch_size = kwargs.get("batch_size", 10000)

    table_count = len(tables)

    total_rows = sum(
        row_counts.get(table, 0)
        for table in tables
    )

    batches = math.ceil(total_rows / batch_size) if total_rows else 0

    print("source:", source)
    print("destination:", destination)
    print("tables:", tables)
    print("table count:", table_count)
    print("total rows:", total_rows)
    print("required batches:", batches)

etl_summary(
    "sql server",
    "adls gen2",
    "customer",
    "orders",
    "products",
    row_counts={
        "customer": 12000,
        "orders": 55000,
        "products": 3000
    },
    batch_size=10000
)
"""


"""
assignment 18: role-based permission checker

requirement:

accept requested actions using *args.

accept user information using **kwargs.

roles and permissions:

admin -> read, write, update, delete

editor -> read, write, update

viewer -> read

print whether every action is allowed or denied.

detailed hints:
- create a dictionary containing role permissions.
- read role using kwargs.get().
- get allowed actions for the role.
- use action in allowed_actions.

def check_permissions(__________, __________):
    role_permissions = {
        "admin": {"read", "write", "update", "delete"},
        "editor": {"read", "write", "update"},
        "viewer": {"read"}
    }

    role = kwargs.get("role", __________)
    allowed_actions = role_permissions.get(role, __________)

    print("user:", kwargs.get("username", "unknown"))
    print("role:", role)

    for action in actions:
        if action in __________:
            print(action, ": allowed")
        else:
            print(action, ": denied")

check_permissions(
    "read",
    "update",
    "delete",
    username="rahul",
    role="editor"
)

expected output:

user: rahul
role: editor
read : allowed
update : allowed
delete : denied
"""

"""
def check_permissions(*actions, **kwargs):
    role_permissions = {
        "admin": {"read", "write", "update", "delete"},
        "editor": {"read", "write", "update"},
        "viewer": {"read"}
    }

    role = kwargs.get("role", "viewer")
    allowed_actions = role_permissions.get(role, set())

    print("user:", kwargs.get("username", "unknown"))
    print("role:", role)

    for action in actions:
        if action in allowed_actions:
            print(action, ": allowed")
        else:
            print(action, ": denied")

check_permissions(
    "read",
    "update",
    "delete",
    username="rahul",
    role="editor"
)
"""


"""
assignment 19: dynamic object creation

requirement:

create an employee class.

accept employee skills using *args.

accept employee properties using **kwargs.

set every keyword argument as an object attribute.

detailed hints:
- store skills in self.skills.
- loop through kwargs.items().
- use setattr(self, key, value).
- use getattr() to safely read attributes.

class employee:

    def __init__(self, __________, __________):
        self.skills = __________

        for key, value in details.__________():
            __________(self, key, value)

    def display(self):
        print("name:", getattr(self, "name", "not provided"))
        print("department:", getattr(self, "department", "not provided"))
        print("skills:", self.skills)

employee = employee(
    "python",
    "sql",
    "azure",
    name="rahul",
    department="data engineering",
    experience=5
)

employee.display()

expected output:

name: rahul
department: data engineering
skills: ('python', 'sql', 'azure')
"""

"""
class Employee:

    def __init__(self, *skills, **details):
        self.skills = skills

        for key, value in details.items():
            setattr(self, key, value)

    def display(self):
        print("name:", getattr(self, "name", "not provided"))
        print("department:", getattr(self, "department", "not provided"))
        print("skills:", self.skills)

employee = Employee(
    "python",
    "sql",
    "azure",
    name="rahul",
    department="data engineering",
    experience=5
)

employee.display()
"""


"""
assignment 20: complex order processor

requirement:

accept:
- order id as a normal argument
- product dictionaries using *args
- customer, discount, tax and payment details using **kwargs

each product dictionary contains:
- name
- price
- quantity

calculate:
1. total quantity
2. subtotal
3. discount amount
4. amount after discount
5. tax amount
6. final payable amount

detailed hints:
- loop through every product.
- product total = price * quantity.
- add quantity to total_quantity.
- add product total to subtotal.
- read discount and tax using kwargs.get().
- use round() while printing.
- validate that each product is a dictionary.

def process_order(order_id, __________, __________):
    subtotal = __________
    total_quantity = __________

    for product in products:
        if not isinstance(product, __________):
            continue

        price = product.get("price", __________)
        quantity = product.get("quantity", __________)

        product_total = __________ * __________

        subtotal += __________
        total_quantity += __________

    discount_percentage = kwargs.get("discount", 0)
    tax_percentage = kwargs.get("tax", 0)

    discount_amount = subtotal * __________ / 100
    amount_after_discount = __________ - __________

    tax_amount = amount_after_discount * __________ / 100
    final_amount = __________ + __________

    print("order id:", order_id)
    print("customer:", kwargs.get("customer", "guest"))
    print("payment mode:", kwargs.get("payment_mode", "not provided"))
    print("total quantity:", total_quantity)
    print("subtotal:", round(subtotal, 2))
    print("discount amount:", round(discount_amount, 2))
    print("tax amount:", round(tax_amount, 2))
    print("final amount:", round(final_amount, 2))

process_order(
    "ord-1001",
    {"name": "laptop", "price": 50000, "quantity": 1},
    {"name": "mouse", "price": 1000, "quantity": 2},
    {"name": "keyboard", "price": 2000, "quantity": 1},
    customer="rahul",
    payment_mode="upi",
    discount=10,
    tax=18
)

expected output:

order id: ord-1001
customer: rahul
payment mode: upi
total quantity: 4
subtotal: 54000
discount amount: 5400.0
tax amount: 8748.0
final amount: 57348.0
"""

"""
def process_order(order_id, *products, **kwargs):
    subtotal = 0
    total_quantity = 0

    for product in products:
        if not isinstance(product, dict):
            continue

        price = product.get("price", 0)
        quantity = product.get("quantity", 0)

        product_total = price * quantity

        subtotal += product_total
        total_quantity += quantity

    discount_percentage = kwargs.get("discount", 0)
    tax_percentage = kwargs.get("tax", 0)

    discount_amount = subtotal * discount_percentage / 100
    amount_after_discount = subtotal - discount_amount

    tax_amount = amount_after_discount * tax_percentage / 100
    final_amount = amount_after_discount + tax_amount

    print("order id:", order_id)
    print("customer:", kwargs.get("customer", "guest"))
    print("payment mode:", kwargs.get("payment_mode", "not provided"))
    print("total quantity:", total_quantity)
    print("subtotal:", round(subtotal, 2))
    print("discount amount:", round(discount_amount, 2))
    print("tax amount:", round(tax_amount, 2))
    print("final amount:", round(final_amount, 2))

process_order(
    "ord-1001",
    {"name": "laptop", "price": 50000, "quantity": 1},
    {"name": "mouse", "price": 1000, "quantity": 2},
    {"name": "keyboard", "price": 2000, "quantity": 1},
    customer="rahul",
    payment_mode="upi",
    discount=10,
    tax=18
)
"""

