from functools import reduce

"""
reduce question 1
numbers=[10,20,30,40,50]
using reduce(), calculate the sum of all numbers.
"""
"""
numbers=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,numbers)
print(result)
"""

"""
reduce question 2
numbers=[2,3,4,5]
using reduce(), calculate the product of all numbers.
"""
"""
numbers=[2,3,4,5]
result=reduce(lambda x,y:x*y,numbers)
print(result)
"""

"""
reduce question 3
numbers=[45,12,89,34,67,91,28]
using reduce(), find the maximum number.
"""
"""
numbers=[45,12,89,34,67,91,28]
result=reduce(lambda x,y:x if x>y else y,numbers)
print(result)
"""

"""
reduce question 4
numbers=[45,12,89,34,67,91,28]
using reduce(), find the minimum number.
"""
"""
numbers=[45,12,89,34,67,91,28]
result=reduce(lambda x,y:x if x<y else y,numbers)
print(result)
"""

"""
reduce question 5
words=["python"," ","is"," ","powerful"]
using reduce(), combine all strings into one sentence.
"""
"""
words=["python"," ","is"," ","powerful"]
result=reduce(lambda x,y:x+y,words)
print(result)
"""

"""
reduce question 6
words=["python","azure","cloud","ai"]
using reduce(), calculate total number of characters in all words.
"""
"""
words=["python","azure","cloud","ai"]
result=reduce(lambda x,y:x+len(y),words,0)
print(result)
"""

"""
reduce question 7
number=6
numbers=list(range(1,number+1))
using reduce(), calculate factorial of number.
"""
"""
number=6
numbers=list(range(1,number+1))
result=reduce(lambda x,y:x*y,numbers)
print(result)
"""

"""
reduce question 8
numbers=[12,45,67,89,23,56,91,34,78,100]
using reduce(), calculate sum of only even numbers.
"""
"""
numbers=[12,45,67,89,23,56,91,34,78,100]
result=reduce(lambda x,y:x+y if y%2==0 else x,numbers,0)
print(result)
"""

"""
reduce question 9
numbers=[12,45,67,89,23,56,91,34,78,100]
using reduce(), calculate sum of only odd numbers.
"""
"""
numbers=[12,45,67,89,23,56,91,34,78,100]
result=reduce(lambda x,y:x+y if y%2!=0 else x,numbers,0)
print(result)
"""

"""
reduce question 10
words=["ai","python","databricks","cloud","kubernetes"]
using reduce(), find the longest word.
"""
"""
words=["ai","python","databricks","cloud","kubernetes"]
result=reduce(lambda x,y:x if len(x)>len(y) else y,words)
print(result)
"""

"""
reduce question 11
words=["ai","python","databricks","cloud","kubernetes"]
using reduce(), find the shortest word.
"""
"""
words=["ai","python","databricks","cloud","kubernetes"]
result=reduce(lambda x,y:x if len(x)<len(y) else y,words)
print(result)
"""

"""
reduce question 12
salaries=[45000,65000,72000,82000,55000]
using reduce(), calculate total salary.
"""
"""
salaries=[45000,65000,72000,82000,55000]
result=reduce(lambda x,y:x+y,salaries)
print(result)
"""

"""
reduce question 13
employees=[{"name":"rahul","salary":45000},{"name":"anil","salary":65000},{"name":"sneha","salary":72000},{"name":"kiran","salary":82000},{"name":"meena","salary":55000}]
using reduce(), calculate total payroll directly from dictionaries.
"""
"""
employees=[{"name":"rahul","salary":45000},{"name":"anil","salary":65000},{"name":"sneha","salary":72000},{"name":"kiran","salary":82000},{"name":"meena","salary":55000}]
result=reduce(lambda x,y:x+y["salary"],employees,0)
print(result)
"""

"""
reduce question 14
employees=[{"name":"rahul","salary":45000},{"name":"anil","salary":65000},{"name":"sneha","salary":72000},{"name":"kiran","salary":82000},{"name":"meena","salary":55000}]
using reduce(), find employee with highest salary.
"""
"""
employees=[{"name":"rahul","salary":45000},{"name":"anil","salary":65000},{"name":"sneha","salary":72000},{"name":"kiran","salary":82000},{"name":"meena","salary":55000}]
result=reduce(lambda x,y:x if x["salary"]>y["salary"] else y,employees)
print(result)
"""

"""
reduce question 15
students=[{"name":"ravi","marks":92},{"name":"kiran","marks":68},{"name":"meena","marks":85},{"name":"ajay","marks":48},{"name":"rahul","marks":95}]
using reduce(), find student with highest marks.
"""
"""
students=[{"name":"ravi","marks":92},{"name":"kiran","marks":68},{"name":"meena","marks":85},{"name":"ajay","marks":48},{"name":"rahul","marks":95}]
result=reduce(lambda x,y:x if x["marks"]>y["marks"] else y,students)
print(result)
"""

"""
reduce question 16
products=[{"name":"laptop","price":55000,"stock":5},{"name":"mouse","price":600,"stock":25},{"name":"keyboard","price":1500,"stock":15},{"name":"monitor","price":18000,"stock":8}]
using reduce(), calculate total stock quantity.
"""
"""
products=[{"name":"laptop","price":55000,"stock":5},{"name":"mouse","price":600,"stock":25},{"name":"keyboard","price":1500,"stock":15},{"name":"monitor","price":18000,"stock":8}]
result=reduce(lambda x,y:x+y["stock"],products,0)
print(result)
"""

"""
reduce question 17
products=[{"name":"laptop","price":55000,"stock":5},{"name":"mouse","price":600,"stock":25},{"name":"keyboard","price":1500,"stock":15},{"name":"monitor","price":18000,"stock":8}]
using reduce(), calculate total inventory value using price*stock.
"""
"""
products=[{"name":"laptop","price":55000,"stock":5},{"name":"mouse","price":600,"stock":25},{"name":"keyboard","price":1500,"stock":15},{"name":"monitor","price":18000,"stock":8}]
result=reduce(lambda x,y:x+(y["price"]*y["stock"]),products,0)
print(result)
"""

"""
reduce question 18
sales=[12000,25000,18000,45000,30000,52000]
using reduce(), calculate total sales amount.
"""
"""
sales=[12000,25000,18000,45000,30000,52000]
result=reduce(lambda x,y:x+y,sales)
print(result)
"""

"""
reduce question 19
dictionaries=[{"name":"rahul"},{"age":30},{"department":"it"},{"salary":65000}]
using reduce(), merge all dictionaries into one dictionary.
"""
"""
dictionaries=[{"name":"rahul"},{"age":30},{"department":"it"},{"salary":65000}]
result=reduce(lambda x,y:{**x,**y},dictionaries)
print(result)
"""

"""
reduce question 20
numbers=[12,45,12,67,45,89,23,67,100]
using reduce(), calculate sum of unique numbers only.
"""
"""
numbers=[12,45,12,67,45,89,23,67,100]
result=reduce(lambda x,y:x if y in x else x+[y],numbers,[])
print(sum(result))
"""