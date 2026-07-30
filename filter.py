"""
filter question 1
numbers = [12,45,67,89,23,56,91,34,78,100]
using filter(), extract all even numbers.
"""
"""
numbers=[12,45,67,89,23,56,91,34,78,100]
result=list(filter(lambda x:x%2==0,numbers))
print(result)
"""

"""
filter question 2
numbers = [12,45,67,89,23,56,91,34,78,100]
using filter(), extract all odd numbers.
"""
"""
numbers=[12,45,67,89,23,56,91,34,78,100]
result=list(filter(lambda x:x%2!=0,numbers))
print(result)
"""

"""
filter question 3
numbers = [12,45,67,89,23,56,91,34,78,100]
using filter(), extract all numbers greater than 50.
"""
"""
numbers=[12,45,67,89,23,56,91,34,78,100]
result=list(filter(lambda x:x>50,numbers))
print(result)
"""

"""
filter question 4
numbers = [120,45,167,89,230,56,91,34,178,100]
using filter(), extract all numbers less than 100.
"""
"""
numbers=[120,45,167,89,230,56,91,34,178,100]
result=list(filter(lambda x:x<100,numbers))
print(result)
"""

"""
filter question 5
numbers = [-15,-8,0,4,12,-25,37,42]
using filter(), extract all positive numbers.
"""
"""
numbers=[-15,-8,0,4,12,-25,37,42]
result=list(filter(lambda x:x>0,numbers))
print(result)
"""

"""
filter question 6
numbers = [-15,-8,0,4,12,-25,37,42]
using filter(), extract all negative numbers.
"""
"""
numbers=[-15,-8,0,4,12,-25,37,42]
result=list(filter(lambda x:x<0,numbers))
print(result)
"""

"""
filter question 7
numbers = [-15,-8,0,4,12,0,-25,37,0]
using filter(), remove all zero values.
"""
"""
numbers=[-15,-8,0,4,12,0,-25,37,0]
result=list(filter(lambda x:x!=0,numbers))
print(result)
"""

"""
filter question 8
words=["python","azure","ai","developer","cloud","analytics"]
using filter(), extract words containing more than five characters.
"""
"""
words=["python","azure","ai","developer","cloud","analytics"]
result=list(filter(lambda x:len(x)>5,words))
print(result)
"""

"""
filter question 9
names=["anil","rahul","ajay","meena","arjun","kiran","akhil"]
using filter(), extract names beginning with a.
"""
"""
names=["anil","rahul","ajay","meena","arjun","kiran","akhil"]
result=list(filter(lambda x:x.startswith("a"),names))
print(result)
"""

"""
filter question 10
names=["kiran","mohan","arjun","rajan","meena","varun"]
using filter(), extract names ending with n.
"""
"""
names=["kiran","mohan","arjun","rajan","meena","varun"]
result=list(filter(lambda x:x.endswith("n"),names))
print(result)
"""

"""
filter question 11
numbers=[10,15,18,20,25,30,32,40,45,50]
using filter(), extract all multiples of 5.
"""
"""
numbers=[10,15,18,20,25,30,32,40,45,50]
result=list(filter(lambda x:x%5==0,numbers))
print(result)
"""

"""
filter question 12
numbers=[3,5,10,15,18,30,42,45,60,75]
using filter(), extract numbers divisible by both 3 and 5.
"""
"""
numbers=[3,5,10,15,18,30,42,45,60,75]
result=list(filter(lambda x:x%3==0 and x%5==0,numbers))
print(result)
"""

"""
filter question 13
words=["madam","python","level","azure","radar","cloud","civic"]
using filter(), extract palindrome words.
"""
"""
words=["madam","python","level","azure","radar","cloud","civic"]
result=list(filter(lambda x:x==x[::-1],words))
print(result)
"""

"""
filter question 14
emails=["john@gmail.com","rahul@yahoo.com","admin@python.com","support@azure.org","sales@company.com"]
using filter(), extract email addresses ending with .com.
"""
"""
emails=["john@gmail.com","rahul@yahoo.com","admin@python.com","support@azure.org","sales@company.com"]
result=list(filter(lambda x:x.endswith(".com"),emails))
print(result)
"""

"""
filter question 15
files=["sales.csv","employees.xlsx","products.csv","report.pdf","customers.csv","notes.txt"]
using filter(), extract all csv files.
"""
"""
files=["sales.csv","employees.xlsx","products.csv","report.pdf","customers.csv","notes.txt"]
result=list(filter(lambda x:x.endswith(".csv"),files))
print(result)
"""

"""
filter question 16
using filter(), extract employees whose salary is greater than 60000.
"""
"""
employees=[
{"name":"rahul","salary":45000},
{"name":"anil","salary":65000},
{"name":"sneha","salary":72000},
{"name":"kiran","salary":82000},
{"name":"meena","salary":55000}
]
result=list(filter(lambda x:x["salary"]>60000,employees))
print(result)
"""

"""
filter question 17
using filter(), extract students who scored more than 80.
"""
"""
students=[
{"name":"ravi","marks":92},
{"name":"kiran","marks":68},
{"name":"meena","marks":85},
{"name":"ajay","marks":48},
{"name":"sneha","marks":79}
]
result=list(filter(lambda x:x["marks"]>80,students))
print(result)
"""

"""
filter question 18
using filter(), extract products currently in stock.
"""
"""
products=[
{"name":"laptop","price":55000,"stock":5},
{"name":"mouse","price":600,"stock":25},
{"name":"keyboard","price":1500,"stock":0},
{"name":"monitor","price":18000,"stock":8},
{"name":"printer","price":12000,"stock":0}
]
result=list(filter(lambda x:x["stock"]>0,products))
print(result)
"""

"""
filter question 19
using filter(), extract people eligible to vote.
"""
"""
people=[
{"name":"rahul","age":17},
{"name":"anil","age":25},
{"name":"sneha","age":16},
{"name":"kiran","age":32},
{"name":"meena","age":18}
]
result=list(filter(lambda x:x["age"]>=18,people))
print(result)
"""

"""
filter question 20
using filter(), extract employees belonging to it department and active.
"""
"""
employees=[
{"name":"rahul","department":"it","active":True},
{"name":"anil","department":"hr","active":True},
{"name":"sneha","department":"it","active":False},
{"name":"kiran","department":"it","active":True},
{"name":"meena","department":"sales","active":True}
]
result=list(filter(lambda x:x["department"]=="it" and x["active"],employees))
print(result)
"""