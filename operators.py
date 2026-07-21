# python operators - 30 coding questions
# uncomment only the required question to run

# question 1:
# write a program to perform addition, subtraction,
# multiplication, division, floor division,
# modulus, and exponentiation on two numbers.

"""
a = float(input("enter first number: "))
b = float(input("enter second number: "))

print("addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)
print("floor division:", a // b)
print("modulus:", a % b)
print("exponentiation:", a ** b)
"""


# question 2:
# swap two numbers without using a third variable.

"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))

a = a + b
b = a - b
a = a - b

print("after swapping")
print("a =", a)
print("b =", b)
"""

# question 3:
# find whether a number is even or odd using the modulus operator.

"""
num = int(input("enter a number: "))

if num % 2 == 0:
    print("even")
else:
    print("odd")
"""

# question 4:
# reverse a three-digit number using arithmetic operators.

"""
num = int(input("enter a three digit number: "))

last = num % 10
middle = (num // 10) % 10
first = num // 100

reverse = last * 100 + middle * 10 + first

print("reversed number:", reverse)
"""

# question 5:
# find the last digit and first digit of a given number.

"""
num = int(input("enter a number: "))

last = num % 10

temp = num
while temp >= 10:
    temp = temp // 10

first = temp

print("first digit:", first)
print("last digit:", last)
"""

# question 6:
# demonstrate all assignment operators
# (=, +=, -=, *=, /=, //=, %= and **=)

"""
num = int(input("enter a number: "))

a = num
print("= :", a)

a += 5
print("+= :", a)

a -= 2
print("-= :", a)

a *= 3
print("*= :", a)

a /= 2
print("/= :", a)

a //= 2
print("//= :", a)

a %= 3
print("%= :", a)

a **= 2
print("**= :", a)
"""

# question 7:
# update a bank account balance using compound assignment operators.

"""
balance = float(input("enter account balance: "))
deposit = float(input("enter deposit amount: "))
withdraw = float(input("enter withdrawal amount: "))

balance += deposit
balance -= withdraw

print("updated balance:", balance)
"""

# question 8:
# calculate the total marks using += inside a loop.

"""
total = 0

n = int(input("enter number of subjects: "))

for i in range(n):
    mark = int(input("enter mark: "))
    total += mark

print("total marks:", total)
"""

# question 9:
# compare two numbers and print the larger number.

"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))

if a > b:
    print("larger number:", a)
elif b > a:
    print("larger number:", b)
else:
    print("both numbers are equal")
"""

# question 10:
# check whether three numbers are equal.

"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a == b and b == c:
    print("all three numbers are equal")
else:
    print("all three numbers are not equal")
"""

# question 11:
# find the largest among three numbers using comparison operators.

"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a > b and a > c:
    print("largest number:", a)
elif b > a and b > c:
    print("largest number:", b)
else:
    print("largest number:", c)
"""

# question 12:
# check whether a student is eligible to vote based on age.

"""
age = int(input("enter age: "))

if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")
"""

# question 13:
# check if a person is eligible for a loan
# (age > 21 and salary > 30000).

"""
age = int(input("enter age: "))
salary = float(input("enter salary: "))

if age > 21 and salary > 30000:
    print("eligible for loan")
else:
    print("not eligible for loan")
"""

# question 14:
# check if a number lies between 10 and 100 using logical operators.

"""
num = int(input("enter a number: "))

if num >= 10 and num <= 100:
    print("number is between 10 and 100")
else:
    print("number is not between 10 and 100")
"""

# question 15:
# validate username and password using logical operators.

"""
username = input("enter username: ")
password = input("enter password: ")

if username == "admin" and password == "1236":
    print("login successful")
else:
    print("invalid username or password")
"""

# question 16:
# determine whether a year is a leap year using logical conditions.

"""
year = int(input("enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("not a leap year")
"""

# question 17:
# find the bitwise and, or, xor of two numbers

"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))

print("bitwise and:", a & b)
print("bitwise or:", a | b)
print("bitwise xor:", a ^ b)
"""

# question 18:
# perform left shift and right shift operations.

"""
num = int(input("enter a number: "))
shift = int(input("enter number of positions: "))

print("left shift:", num << shift)
print("right shift:", num >> shift)
"""

# question 19:
# check whether a number is even using a bitwise operator.

"""
num = int(input("enter a number: "))

if (num & 1) == 0:
    print("even")
else:
    print("odd")
"""

# question 20:
# swap two numbers using the xor operator.

"""
a = int(input("enter first number: "))
b = int(input("enter second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("after swapping")
print("a =", a)
print("b =", b)
"""

# question 21:
# count how many bits are set to 1 in a number using bitwise operations.

"""
num = int(input("enter a number: "))

count = 0

while num > 0:
    if num & 1:
        count += 1
    num = num >> 1

print("number of set bits:", count)
"""

# question 22:
# demonstrate the difference between is and ==.

"""
a = [1, 2, 3]
b = [1, 2, 3]

print("using == :", a == b)
print("using is :", a is b)
"""

# question 23:
# check whether two variables refer to the same list object.

"""
list1 = [10, 20, 30]
list2 = list1

if list1 is list2:
    print("both variables refer to the same list")
else:
    print("both variables refer to different lists")
"""

# question 24:
# show the behavior of is not with integers and lists.

"""
a = 10
b = 20

print("integers")

if a is not b:
    print("a is not b")
else:
    print("a is b")

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("lists")

if list1 is not list2:
    print("list1 is not list2")
else:
    print("list1 is list2")
"""

# question 25:
# check whether a character exists in a string.

"""
text = input("enter a string: ")
ch = input("enter a character: ")

if ch in text:
    print("character found")
else:
    print("character not found")
"""

# question 26:
# check whether a number exists in a list.

"""
numbers = []

n = int(input("enter number of elements: "))

for i in range(n):
    value = int(input("enter number: "))
    numbers.append(value)

search = int(input("enter number to search: "))

if search in numbers:
    print("number found")
else:
    print("number not found")
"""

# question 27:
# count how many vowels in a string belong to a predefined vowel list using in.

"""
text = input("enter a string: ")

vowels = "aeiou"

count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("number of vowels:", count)
"""

# question 28:
# build a simple calculator using arithmetic and comparison operators.

"""
a = float(input("enter first number: "))
b = float(input("enter second number: "))
op = input("enter operator (+, -, *, /, //, %, **): ")

if op == "+":
    print("answer:", a + b)
elif op == "-":
    print("answer:", a - b)
elif op == "*":
    print("answer:", a * b)
elif op == "/":
    print("answer:", a / b)
elif op == "//":
    print("answer:", a // b)
elif op == "%":
    print("answer:", a % b)
elif op == "**":
    print("answer:", a ** b)
else:
    print("invalid operator")
"""

# question 29:
# create a grading system using comparison and logical operators.

"""
mark = int(input("enter mark: "))

if mark >= 90 and mark <= 100:
    print("grade a")
elif mark >= 80 and mark < 90:
    print("grade b")
elif mark >= 70 and mark < 80:
    print("grade c")
elif mark >= 60 and mark < 70:
    print("grade d")
elif mark >= 0 and mark < 60:
    print("grade f")
else:
    print("invalid mark")
"""

# question 30:
# build a menu-driven calculator that uses arithmetic,
# comparison, logical, assignment, membership,
# identity, and bitwise operators wherever applicable.

"""
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. modulus")
print("6. floor division")
print("7. exponentiation")
print("8. bitwise and")
print("9. bitwise or")
print("10. bitwise xor")
print("11. left shift")
print("12. right shift")

choice = int(input("enter your choice: "))

a = int(input("enter first number: "))
b = int(input("enter second number: "))

if choice == 1:
    print("answer:", a + b)
elif choice == 2:
    print("answer:", a - b)
elif choice == 3:
    print("answer:", a * b)
elif choice == 4:
    print("answer:", a / b)
elif choice == 5:
    print("answer:", a % b)
elif choice == 6:
    print("answer:", a // b)
elif choice == 7:
    print("answer:", a ** b)
elif choice == 8:
    print("answer:", a & b)
elif choice == 9:
    print("answer:", a | b)
elif choice == 10:
    print("answer:", a ^ b)
elif choice == 11:
    print("answer:", a << b)
elif choice == 12:
    print("answer:", a >> b)
else:
    print("invalid choice") 

"""