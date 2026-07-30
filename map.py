"""
map question 1
numbers = [1,2,3,4,5,6]
using map() and lambda, calculate square of every number.
"""

"""
numbers = [1,2,3,4,5,6]
result = list(map(lambda x:x**2,numbers))
print(result)
"""

"""
map question 2
numbers = [2,3,4,5,6]
using map() and lambda, calculate cube of every number.
"""

"""
numbers = [2,3,4,5,6]
result = list(map(lambda x:x**3,numbers))
print(result)
"""

"""
map question 3
numbers = [10,20,30,40,50]
using map(), add 5 to every number.
"""

"""
numbers = [10,20,30,40,50]
result = list(map(lambda x:x+5,numbers))
print(result)
"""

"""
map question 4
numbers = [15,25,35,45,55]
using map(), subtract 10 from every number.
"""

"""
numbers = [15,25,35,45,55]
result = list(map(lambda x:x-10,numbers))
print(result)
"""

"""
map question 5
numbers = [1,5,10,15,20]
using map(), multiply every number by 100.
"""

"""
numbers = [1,5,10,15,20]
result = list(map(lambda x:x*100,numbers))
print(result)
"""

"""
map question 6
names = ["ravi","anil","meena","kiran","sneha"]
using map(), convert every name to uppercase.
"""

"""
names = ["ravi","anil","meena","kiran","sneha"]
result = list(map(lambda x:x.upper(),names))
print(result)
"""

"""
map question 7
names = ["rahul","divya","arjun","ajay"]
using map(), convert every name to lowercase.
"""

"""
names = ["rahul","divya","arjun","ajay"]
result = list(map(lambda x:x.lower(),names))
print(result)
"""

"""
map question 8
names = ["rahul kumar","anil sharma","meena reddy","divya singh"]
using map(), convert every name to title case.
"""

"""
names = ["rahul kumar","anil sharma","meena reddy","divya singh"]
result = list(map(lambda x:x.title(),names))
print(result)
"""

"""
map question 9
words = ["python","azure","databricks","cloud","ai"]
using map(), calculate length of every word.
"""

"""
words = ["python","azure","databricks","cloud","ai"]
result = list(map(lambda x:len(x),words))
print(result)
"""

"""
map question 10
words = ["python","azure","docker","linux","spark"]
using map(), extract first character of every word.
"""

"""
words = ["python","azure","docker","linux","spark"]
result = list(map(lambda x:x[0],words))
print(result)
"""

"""
map question 11
words = ["python","azure","docker","linux","spark"]
using map(), extract last character of every word.
"""

"""
words = ["python","azure","docker","linux","spark"]
result = list(map(lambda x:x[-1],words))
print(result)
"""

"""
map question 12
temperatures = [0,10,20,30,40]
using map(), convert celsius into fahrenheit.
"""

"""
temperatures = [0,10,20,30,40]
result = list(map(lambda x:(x*9/5)+32,temperatures))
print(result)
"""

"""
map question 13
prices = [100,250,500,1000,2500]
using map(), calculate 18% gst.
"""

"""
prices = [100,250,500,1000,2500]
result = list(map(lambda x:x*18/100,prices))
print(result)
"""

"""
map question 14
prices = [100,250,500,1000,2500]
using map(), calculate final price after gst.
"""

"""
prices = [100,250,500,1000,2500]
result = list(map(lambda x:x+(x*18/100),prices))
print(result)
"""

"""
map question 15
decimal_numbers = [12.4567,45.8976,78.1234,99.9999]
using map(), round every number to two decimal places.
"""

"""
decimal_numbers = [12.4567,45.8976,78.1234,99.9999]
result = list(map(lambda x:round(x,2),decimal_numbers))
print(result)
"""

"""
map question 16
values = [-10,20,-35,40,-55,60]
using map(), convert every number into absolute value.
"""

"""
values = [-10,20,-35,40,-55,60]
result = list(map(lambda x:-x if x<0 else x,values))
print(result)
"""

"""
map question 17
numbers = [10,20,30,40,50]
using map(), convert every integer into string.
"""

"""
numbers = [10,20,30,40,50]
result = list(map(lambda x:str(x),numbers))
print(result)
"""

"""
map question 18
names = [" ravi "," anil","meena "," kiran "]
using map(), remove leading and trailing spaces.
"""

"""
names = [" ravi "," anil","meena "," kiran "]
result = list(map(lambda x:x.strip(),names))
print(result)
"""

"""
map question 19
employees = [
{"id":101,"name":"rahul","salary":45000},
{"id":102,"name":"anil","salary":65000},
{"id":103,"name":"sneha","salary":72000},
{"id":104,"name":"kiran","salary":82000}
]
using map(), extract employee names.
"""

"""
employees = [
{"id":101,"name":"rahul","salary":45000},
{"id":102,"name":"anil","salary":65000},
{"id":103,"name":"sneha","salary":72000},
{"id":104,"name":"kiran","salary":82000}
]
result = list(map(lambda x:x["name"],employees))
print(result)
"""

"""
map question 20
employees = [
{"id":101,"name":"rahul","salary":45000},
{"id":102,"name":"anil","salary":65000},
{"id":103,"name":"sneha","salary":72000},
{"id":104,"name":"kiran","salary":82000}
]
using map(), create new list with name, original salary and updated salary.
"""

"""
employees = [
{"id":101,"name":"rahul","salary":45000},
{"id":102,"name":"anil","salary":65000},
{"id":103,"name":"sneha","salary":72000},
{"id":104,"name":"kiran","salary":82000}
]
result = list(map(lambda x:{"name":x["name"],"original_salary":x["salary"],"updated_salary":x["salary"]*1.10},employees))
print(result)
"""