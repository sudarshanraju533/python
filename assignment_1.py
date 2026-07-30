# -*- coding: utf-8 -*-
"""Practice file for list and nested-list exercises."""

# Run this setup block once before trying any example.
bank = [
    [
        [
            ["C101", "Rahul", "Savings", 85000],
            ["C102", "Anita", "Current", 150000],
            ["C103", "Kiran", "Loan", 500000],
        ],
        [
            ["C104", "Sneha", "Savings", 95000],
            ["C105", "Vikram", "Current", 275000],
            ["C106", "Meena", "Loan", 750000],
        ],
    ],
    [
        [
            ["C201", "Arjun", "Savings", 120000],
            ["C202", "Pooja", "Current", 325000],
            ["C203", "Ramesh", "Loan", 900000],
        ],
        [
            ["C204", "Priya", "Savings", 45000],
            ["C205", "Amit", "Current", 185000],
            ["C206", "Divya", "Loan", 650000],
        ],
    ],
    [
        [
            ["C301", "Nikhil", "Savings", 78000],
            ["C302", "Kavya", "Current", 240000],
            ["C303", "Suresh", "Loan", 1000000],
        ],
        [
            ["C304", "Neha", "Savings", 135000],
            ["C305", "Rohan", "Current", 410000],
            ["C306", "Asha", "Loan", 550000],
        ],
    ],
]

employe = [
    ["E101", "Rahul", "Sales"],
    ["E102", "Anita", "Sales"],
    ["E103", "Kiran", "Finance"],
    ["E104", "Sneha", "Finance"],
    ["E105", "Vikram", "IT"],
]

accounts = ["B101", "B102", "B103"]
customers = [["C101", "Rahul"], ["C102", "Anita"], ["C103", "Kiran"]]
transactions = [1000, 2000, 3000, 5000]
transaction_ids = [101, 102, 103, 104, 105]
balances = [50000, 15000, 75000, 25000]
names = ["Rahul", "Amit", "Sneha", "Priya"]
original = [100, 200, 300]
items = [10, 20, 30, 40]
branches = ["Chennai", "Delhi", "Mumbai"]
new_branches = ["Bangalore", "Hyderabad"]
cities = ["Bangalore", "Chennai", "Bangalore", "Delhi", "Bangalore"]
banks = ["SBI", "HDFC", "ICICI", "Axis"]
loan_amounts = [500000, 250000, 750000, 100000]
balance = [50000, 75000, 50000, 25000]
numbers = [10, 20, 30, 40, 50]

# Uncomment one block at a time and run it.

# 1) Print Rahul's complete record
"""
print(bank[0][0][0])
"""

# 2) Print Anita's account type
"""
print(bank[0][0][1][2])
"""

# 3) Print Kiran's loan amount
"""
print(bank[0][0][2][3])
"""

# 4) Print Sneha's customer ID
"""
print(bank[0][1][0][0])
"""

# 5) Print Vikram's balance
"""
print(bank[0][1][1][3])
"""

# 6) Print Meena's complete record
"""
print(bank[0][1][2])
"""

# 7) Print Arjun's customer ID
"""
print(bank[1][0][0][0])
"""

# 8) Print Pooja's name
"""
print(bank[1][0][1][1])
"""

# 9) Print Ramesh's account type
"""
print(bank[1][0][2][2])
"""

# 10) Print Priya's balance
"""
print(bank[1][1][0][3])
"""

# 11) Print Amit's account type
"""
print(bank[1][1][1][2])
"""

# 12) Print Divya's customer ID
"""
print(bank[1][1][2][0])
"""

# 13) Print Nikhil's account type
"""
print(bank[2][0][0][2])
"""

# 14) Print Kavya's balance
"""
print(bank[2][0][1][3])
"""

# 15) Print Suresh's loan amount
"""
print(bank[2][0][2][3])
"""

# 16) Print Neha's name
"""
print(bank[2][1][0][1])
"""

# 17) Print Rohan's complete record
"""
print(bank[2][1][1])
"""

# 18) Print Asha's account type
"""
print(bank[2][1][2][2])
"""

# 19) Print all customers in Bank 1, Branch 1
"""
print(bank[0][0])
"""

# 20) Print all customers in Bank 1, Branch 2
"""
print(bank[0][1])
"""

# 21) Print all customers in Bank 2, Branch 1
"""
print(bank[1][0])
"""

# 22) Print all customers in Bank 2, Branch 2
"""
print(bank[1][1])
"""

# 23) Print all customers in Bank 3, Branch 1
"""
print(bank[2][0])
"""

# 24) Print all customers in Bank 3, Branch 2
"""
print(bank[2][1])
"""

# 25) Print all branches of Bank 1
"""
print(bank[0])
"""

# 26) Print all branches of Bank 2
"""
print(bank[1])
"""

# 27) Print all branches of Bank 3
"""
print(bank[2])
"""

# 28) Print the first customer from every bank's first branch
"""
print(bank[0][0][0])
print(bank[1][0][0])
print(bank[2][0][0])
"""

# 29) Print the second customer from every bank's second branch
"""
print(bank[0][1][1])
print(bank[1][1][1])
print(bank[2][1][1])
"""

# 30) Print the loan amount of the last customer in Bank 3, Branch 2
"""
print(bank[2][1][2][3])
"""

# 31) Create a list of 5 employee names and add a new employee using append()
"""
employe.append(["E106", "prem", "IT"])
print(employe)
"""

# 32) Create a list of account numbers and add three new account numbers using extend()
"""
accounts.extend(["B104", "B105", "B106"])
print(accounts)
"""

# 33) Insert a new customer at the beginning of a customer list using insert()
"""
customers.insert(0, ["C100", "Priya"])
print(customers)
"""

# 34) Insert a transaction amount at index 3 in a list
"""
transactions.insert(3, 4000)
print(transactions)
"""

# 35) Remove the last item from a list using pop()
"""
removed = transactions.pop()
print(removed)
print(transactions)
"""

# 36) Remove the customer "Rahul" from a customer list using remove()
"""
customers = ["Amit", "Rahul", "Sneha", "Priya"]
customers.remove("Rahul")
print(customers)
"""

# 37) Count how many times the account type "Savings" appears in a list
"""
print(accounts.count("Savings"))
"""

# 38) Find the index of "Current" in a list of account types
"""
print(accounts.index("Current"))
"""

# 39) Reverse a list of transaction IDs using reverse()
"""
transaction_ids.reverse()
print(transaction_ids)
"""

# 40) Sort a list of account balances in ascending order
"""
balances.sort()
print(balances)
"""

# 41) Sort a list of customer names in descending order
"""
names.sort(reverse=True)
print(names)
"""

# 42) Make a copy of a list and verify modifications do not affect original
"""
copied = original.copy()
copied.append(400)
print(original)
print(copied)
"""

# 43) Clear all elements from a list using clear()
"""
items.clear()
print(items)
"""

# 44) Extend a list of branch names with another list of new branches
"""
branches.extend(new_branches)
print(branches)
"""

# 45) Append a nested list containing a new customer's details
"""
customers = [["Amit", 101], ["Sneha", 102]]
customers.append(["Rahul", 103])
print(customers)
"""

# 46) Remove the first occurrence of the balance 50000
"""
balance.remove(50000)
print(balance)
"""

# 47) Pop the element at index 2 and print the removed value
"""
removed = numbers.pop(2)
print(removed)
print(numbers)
"""

# 48) Count how many times the city "Bangalore" appears in a list
"""
print(cities.count("Bangalore"))
"""

# 49) Reverse a list of bank names and print the result
"""
banks.reverse()
print(banks)
"""

# 50) Create a list of loan amounts and sort it in descending order
"""
loan_amounts.sort(reverse=True)
print(loan_amounts)
"""
