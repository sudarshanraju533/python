from functools import reduce

"""
combined question 1
numbers=[12,45,67,89,23,56,91,34,78,100]
using filter() and map():
extract even numbers and calculate square of every even number.
"""
"""
numbers=[12,45,67,89,23,56,91,34,78,100]
even=list(filter(lambda x:x%2==0,numbers))
result=list(map(lambda x:x**2,even))
print(result)
"""

"""
combined question 2
numbers=[12,45,67,89,23,56,91,34,78,100]
using filter() and reduce():
extract odd numbers and calculate their total sum.
"""
"""
numbers=[12,45,67,89,23,56,91,34,78,100]
odd=list(filter(lambda x:x%2!=0,numbers))
result=reduce(lambda x,y:x+y,odd)
print(result)
"""

"""
combined question 3
numbers=[10,25,40,55,70,85,100]
using filter() and map():
extract numbers greater than 50 and multiply every selected number by 2.
"""
"""
numbers=[10,25,40,55,70,85,100]
greater=list(filter(lambda x:x>50,numbers))
result=list(map(lambda x:x*2,greater))
print(result)
"""

"""
combined question 4
numbers=[-15,20,-35,40,50,-10,60]
using filter(), map(), and reduce():
extract positive numbers, calculate square and find total sum.
"""
"""
numbers=[-15,20,-35,40,50,-10,60]
positive=list(filter(lambda x:x>0,numbers))
square=list(map(lambda x:x**2,positive))
result=reduce(lambda x,y:x+y,square)
print(result)
"""

"""
combined question 5
words=["python","azure","ai","developer","cloud","analytics","spark"]
using filter() and map():
extract words containing more than five characters and convert to uppercase.
"""
"""
words=["python","azure","ai","developer","cloud","analytics","spark"]
selected=list(filter(lambda x:len(x)>5,words))
result=list(map(lambda x:x.upper(),selected))
print(result)
"""

"""
combined question 6
names=["Anil","Rahul","Ajay","Meena","Arjun","Kiran","Akhil"]
using filter() and map():
extract names beginning with A and convert to lowercase.
"""
"""
names=["Anil","Rahul","Ajay","Meena","Arjun","Kiran","Akhil"]
selected=list(filter(lambda x:x.startswith("A"),names))
result=list(map(lambda x:x.lower(),selected))
print(result)
"""

"""
combined question 7
numbers=[3,5,10,15,18,30,42,45,60,75]
using filter() and reduce():
extract numbers divisible by both 3 and 5 and calculate total sum.
"""
"""
numbers=[3,5,10,15,18,30,42,45,60,75]
selected=list(filter(lambda x:x%3==0 and x%5==0,numbers))
result=reduce(lambda x,y:x+y,selected)
print(result)
"""

"""
combined question 8
words=["madam","python","level","azure","radar","cloud","civic"]
using filter() and reduce():
extract palindrome words and join using " | ".
"""
"""
words=["madam","python","level","azure","radar","cloud","civic"]
palindrome=list(filter(lambda x:x==x[::-1],words))
result=reduce(lambda x,y:x+" | "+y,palindrome)
print(result)
"""

"""
combined question 9
temperatures=[18,24,30,35,40,12,28,33,15,42]
using filter(), map(), and reduce():
extract temperatures greater than 30,
convert to fahrenheit and calculate average.
"""
"""
temperatures=[18,24,30,35,40,12,28,33,15,42]
selected=list(filter(lambda x:x>30,temperatures))
fahrenheit=list(map(lambda x:(x*9/5)+32,selected))
total=reduce(lambda x,y:x+y,fahrenheit)
result=total/len(fahrenheit)
print(result)
"""

"""
combined question 10
prices=[450,1200,2500,800,5000,1500,7500]
using filter(), map(), and reduce():
extract prices greater than 1000,
apply 10% discount and calculate total.
"""
"""
prices=[450,1200,2500,800,5000,1500,7500]
selected=list(filter(lambda x:x>1000,prices))
discount=list(map(lambda x:x-(x*10/100),selected))
result=reduce(lambda x,y:x+y,discount)
print(result)
"""

"""
combined question 11
employees=[
{"id":101,"name":"Rahul","salary":45000},
{"id":102,"name":"Anil","salary":65000},
{"id":103,"name":"Sneha","salary":72000},
{"id":104,"name":"Kiran","salary":82000},
{"id":105,"name":"Meena","salary":55000}
]

using filter() and map():
extract employees earning more than 60000,
increase salary by 10% and return name with updated salary.
"""
"""
employees=[
{"id":101,"name":"Rahul","salary":45000},
{"id":102,"name":"Anil","salary":65000},
{"id":103,"name":"Sneha","salary":72000},
{"id":104,"name":"Kiran","salary":82000},
{"id":105,"name":"Meena","salary":55000}
]

selected=list(filter(lambda x:x["salary"]>60000,employees))

result=list(map(lambda x:{
"name":x["name"],
"updated_salary":x["salary"]*1.10
},selected))

print(result)
"""

"""
combined question 12
employees=[
{"id":101,"name":"Rahul","department":"IT","salary":45000},
{"id":102,"name":"Anil","department":"HR","salary":65000},
{"id":103,"name":"Sneha","department":"IT","salary":72000},
{"id":104,"name":"Kiran","department":"IT","salary":82000},
{"id":105,"name":"Meena","department":"Sales","salary":55000}
]

using filter() and reduce():
extract IT employees and calculate total salary.
"""
"""
employees=[
{"id":101,"name":"Rahul","department":"IT","salary":45000},
{"id":102,"name":"Anil","department":"HR","salary":65000},
{"id":103,"name":"Sneha","department":"IT","salary":72000},
{"id":104,"name":"Kiran","department":"IT","salary":82000},
{"id":105,"name":"Meena","department":"Sales","salary":55000}
]

selected=list(filter(lambda x:x["department"]=="IT",employees))

result=reduce(lambda x,y:x+y["salary"],selected,0)

print(result)
"""

"""
combined question 13
employees=[
{"id":101,"name":"Rahul","salary":45000,"active":True},
{"id":102,"name":"Anil","salary":65000,"active":True},
{"id":103,"name":"Sneha","salary":72000,"active":False},
{"id":104,"name":"Kiran","salary":82000,"active":True},
{"id":105,"name":"Meena","salary":55000,"active":True},
{"id":106,"name":"Arjun","salary":98000,"active":False}
]

using filter(), map(), and reduce():
extract active employees,
increase salary by 15% and calculate total payroll.
"""
"""
employees=[
{"id":101,"name":"Rahul","salary":45000,"active":True},
{"id":102,"name":"Anil","salary":65000,"active":True},
{"id":103,"name":"Sneha","salary":72000,"active":False},
{"id":104,"name":"Kiran","salary":82000,"active":True},
{"id":105,"name":"Meena","salary":55000,"active":True},
{"id":106,"name":"Arjun","salary":98000,"active":False}
]

active=list(filter(lambda x:x["active"],employees))

updated=list(map(lambda x:x["salary"]*1.15,active))

result=reduce(lambda x,y:x+y,updated)

print(result)
"""

"""
combined question 14
students=[
{"name":"Ravi","marks":92,"passed":True},
{"name":"Kiran","marks":68,"passed":True},
{"name":"Meena","marks":85,"passed":True},
{"name":"Ajay","marks":48,"passed":True},
{"name":"Sneha","marks":35,"passed":False},
{"name":"Rahul","marks":95,"passed":True}
]

using filter() and reduce():
extract passed students and find topper.
"""
"""
students=[
{"name":"Ravi","marks":92,"passed":True},
{"name":"Kiran","marks":68,"passed":True},
{"name":"Meena","marks":85,"passed":True},
{"name":"Ajay","marks":48,"passed":True},
{"name":"Sneha","marks":35,"passed":False},
{"name":"Rahul","marks":95,"passed":True}
]

passed=list(filter(lambda x:x["passed"],students))

result=reduce(lambda x,y:x if x["marks"]>y["marks"] else y,passed)

print(result)
"""

"""
combined question 15
students=[
{"name":"Ravi","marks":92},
{"name":"Kiran","marks":68},
{"name":"Meena","marks":85},
{"name":"Ajay","marks":48},
{"name":"Sneha","marks":79},
{"name":"Rahul","marks":95}
]

using filter(), map(), and reduce():
extract students scoring more than 70,
extract marks and calculate average.
"""
"""
students=[
{"name":"Ravi","marks":92},
{"name":"Kiran","marks":68},
{"name":"Meena","marks":85},
{"name":"Ajay","marks":48},
{"name":"Sneha","marks":79},
{"name":"Rahul","marks":95}
]

selected=list(filter(lambda x:x["marks"]>70,students))

marks=list(map(lambda x:x["marks"],selected))

total=reduce(lambda x,y:x+y,marks)

result=total/len(marks)

print(result)
"""

"""
combined question 16
products=[
{"name":"Laptop","price":55000,"stock":5},
{"name":"Mouse","price":600,"stock":25},
{"name":"Keyboard","price":1500,"stock":0},
{"name":"Monitor","price":18000,"stock":8},
{"name":"Printer","price":12000,"stock":0},
{"name":"SSD","price":6500,"stock":12}
]

using filter(), map(), and reduce():
extract products in stock,
calculate inventory value using price*stock and total value.
"""
"""
products=[
{"name":"Laptop","price":55000,"stock":5},
{"name":"Mouse","price":600,"stock":25},
{"name":"Keyboard","price":1500,"stock":0},
{"name":"Monitor","price":18000,"stock":8},
{"name":"Printer","price":12000,"stock":0},
{"name":"SSD","price":6500,"stock":12}
]

selected=list(filter(lambda x:x["stock"]>0,products))

values=list(map(lambda x:x["price"]*x["stock"],selected))

result=reduce(lambda x,y:x+y,values)

print(result)
"""

"""
combined question 17
products=[
{"name":"Laptop","price":55000,"category":"Electronics"},
{"name":"Chair","price":4500,"category":"Furniture"},
{"name":"Monitor","price":18000,"category":"Electronics"},
{"name":"Desk","price":8500,"category":"Furniture"},
{"name":"SSD","price":6500,"category":"Electronics"}
]

using filter(), map(), and reduce():
extract Electronics products,
apply 20% discount and calculate total discounted value.
"""
"""
products=[
{"name":"Laptop","price":55000,"category":"Electronics"},
{"name":"Chair","price":4500,"category":"Furniture"},
{"name":"Monitor","price":18000,"category":"Electronics"},
{"name":"Desk","price":8500,"category":"Furniture"},
{"name":"SSD","price":6500,"category":"Electronics"}
]

selected=list(filter(lambda x:x["category"]=="Electronics",products))

discount=list(map(lambda x:x["price"]-(x["price"]*20/100),selected))

result=reduce(lambda x,y:x+y,discount)

print(result)
"""

"""
combined question 18
orders=[
{"order_id":1001,"amount":1200,"status":"Delivered"},
{"order_id":1002,"amount":3500,"status":"Pending"},
{"order_id":1003,"amount":8500,"status":"Delivered"},
{"order_id":1004,"amount":4200,"status":"Cancelled"},
{"order_id":1005,"amount":7600,"status":"Delivered"},
{"order_id":1006,"amount":5100,"status":"Pending"}
]

using filter() and reduce():
extract delivered orders and calculate total revenue.
"""
"""
orders=[
{"order_id":1001,"amount":1200,"status":"Delivered"},
{"order_id":1002,"amount":3500,"status":"Pending"},
{"order_id":1003,"amount":8500,"status":"Delivered"},
{"order_id":1004,"amount":4200,"status":"Cancelled"},
{"order_id":1005,"amount":7600,"status":"Delivered"},
{"order_id":1006,"amount":5100,"status":"Pending"}
]

selected=list(filter(lambda x:x["status"]=="Delivered",orders))

result=reduce(lambda x,y:x+y["amount"],selected,0)

print(result)
"""

"""
combined question 19
transactions=[
{"id":1,"amount":1200},
{"id":2,"amount":5200},
{"id":3,"amount":18000},
{"id":4,"amount":2500},
{"id":5,"amount":9600},
{"id":6,"amount":7200}
]

using filter(), map(), and reduce():
extract transactions above 5000,
add 18% GST and calculate total.
"""
"""
transactions=[
{"id":1,"amount":1200},
{"id":2,"amount":5200},
{"id":3,"amount":18000},
{"id":4,"amount":2500},
{"id":5,"amount":9600},
{"id":6,"amount":7200}
]

selected=list(filter(lambda x:x["amount"]>5000,transactions))

gst=list(map(lambda x:x["amount"]+(x["amount"]*18/100),selected))

result=reduce(lambda x,y:x+y,gst)

print(result)
"""

"""
combined question 20
sales_records=[
{"salesperson":"Rahul","region":"South","sales":45000,"active":True},
{"salesperson":"Anil","region":"North","sales":65000,"active":True},
{"salesperson":"Sneha","region":"South","sales":72000,"active":False},
{"salesperson":"Kiran","region":"South","sales":82000,"active":True},
{"salesperson":"Meena","region":"West","sales":55000,"active":True},
{"salesperson":"Arjun","region":"South","sales":98000,"active":True}
]

using filter(), map(), and reduce():
extract active South salespeople,
calculate 5% incentive,
create list with name,sales,incentive and total incentive.
"""
"""
sales_records=[
{"salesperson":"Rahul","region":"South","sales":45000,"active":True},
{"salesperson":"Anil","region":"North","sales":65000,"active":True},
{"salesperson":"Sneha","region":"South","sales":72000,"active":False},
{"salesperson":"Kiran","region":"South","sales":82000,"active":True},
{"salesperson":"Meena","region":"West","sales":55000,"active":True},
{"salesperson":"Arjun","region":"South","sales":98000,"active":True}
]

selected=list(filter(lambda x:x["region"]=="South" and x["active"],sales_records))

result=list(map(lambda x:{
"name":x["salesperson"],
"sales":x["sales"],
"incentive":x["sales"]*5/100
},selected))

total=reduce(lambda x,y:x+y["incentive"],result,0)

print(result)
print(total)
"""