# =========================
# For Loop Assignments
# =========================

# Assignment 36
# Question: Print numbers 1 through 5 on one line using `range`.
# Hint: Use `range(1, 6)` — end is exclusive.

"""
for i in range(1, 6):
    print(i, end=' ')
print()
"""

# Assignment 37
# Question: Sum integers from 1 to 20 and print the result.
# Hint: Same accumulator; change range upper bound to 21.

"""
total = 0
for i in range(1, 21):
    total += i
print(total)
"""

# Assignment 38
# Question: Print the 5-times table from `5 x 1` through `5 x 10`.
# Hint: Set `n = 5` and loop `range(1, 11)`.

"""
n = 5
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
"""

# Assignment 39
# Question: Given `fruits = ['apple','banana','cherry']`, print each fruit with `'Yum: '` prefix.
# Hint: for fruit in fruits: print(...)

"""
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f'Yum: {fruit}')
"""

# Assignment 40
# Question: Count vowels in `'education'` by looping characters and checking `in 'aeiou'`.
# Hint: Increment a counter when ch.lower() is a vowel.

"""
word = 'education'
count = 0
for ch in word:
    if ch.lower() in 'aeiou':
        count += 1
print(count)
"""

# Assignment 41
# Question: Print `'Item 0: x'` style lines for list `['a','b','c']` using enumerate.
# Hint: for i, val in enumerate(lst): ...

"""
lst = ['a', 'b', 'c']
for i, val in enumerate(lst):
    print(f'Item {i}: {val}')
"""

# Assignment 42
# Question: Zip `cities` and `populations` and print `'City: pop'` per pair.
# Hint: Define two equal-length lists and zip in for.

"""
cities = ['Delhi', 'Paris']
populations = [32000000, 2140000]
for city, pop in zip(cities, populations):
    print(f'{city}: {pop}')
"""

# Assignment 43
# Question: Print odd numbers from 1 to 15 using range with step 2.
# Hint: range(1, 16, 2)

"""
for i in range(1, 16, 2):
    print(i, end=' ')
print()
"""

# Assignment 44
# Question: Count down from 10 to 1, then print `'Done'`.
# Hint: range(10, 0, -1)

"""
for i in range(10, 0, -1):
    print(i, end=' ')
print('Done')
"""

# Assignment 45
# Question: Count how many strings in `words` have length > 4.
# Hint: Loop and if len(w) > 4: count += 1

"""
words = ['apple', 'kiwi', 'banana', 'pear']
count = 0
for w in words:
    if len(w) > 4:
        count += 1
print(count)
"""

# Assignment 46
# Question: Find the minimum value in `values = [12, -3, 45, 0, 7]`.
# Hint: Mirror max logic with `<` and min variable.

"""
values = [12, -3, 45, 0, 7]
minimum = values[0]
for value in values:
    if value < minimum:
        minimum = value
print(minimum)
"""

# Assignment 47
# Question: Count how many numbers in `[1,2,2,3,2,4]` are equal to 2.
# Hint: Classic tally loop.

"""
numbers = [1, 2, 2, 3, 2, 4]
tally = 0
for n in numbers:
    if n == 2:
        tally += 1
print(tally)
"""

# Assignment 48
# Question: Search `words` for `'Python'`; print `'Found'` and break, or `'Not found'` after loop.
# Hint: for-else: else runs only if no break.

"""
words = ['Java', 'Python', 'C++']
for word in words:
    if word == 'Python':
        print('Found')
        break
else:
    print('Not found')
"""

# Assignment 49
# Question: Print numbers 1–10 except multiples of 3 (use continue).
# Hint: if i % 3 == 0: continue

"""
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
"""

# Assignment 50
# Question: Print a 5×5 star rectangle using nested loops (`'*'` and print).
# Hint: Outer 5 rows, inner 5 stars per row.

"""
for row in range(5):
    for col in range(5):
        print('*', end='')
    print()
"""

# Assignment 51
# Question: Print each key in `prices = {'apple': 1, 'banana': 2}`.
# Hint: for item in prices: print(item)

"""
prices = {'apple': 1, 'banana': 2}
for item in prices:
    print(item)
"""

# Assignment 52
# Question: Print all values in `ages = {'Ana': 10, 'Bo': 12}`.
# Hint: for v in ages.values():

"""
ages = {'Ana': 10, 'Bo': 12}
for value in ages.values():
    print(value)
"""

# Assignment 53
# Question: Print `'key → value'` for every entry in a dict you define.
# Hint: for k, v in my_dict.items():

"""
my_dict = {'one': 1, 'two': 2}
for k, v in my_dict.items():
    print(f'{k} -> {v}')
"""

# Assignment 54
# Question: Build a list of cubes for n in 1..5 using a for loop.
# Hint: append(n**3) each iteration.

"""
cubes = []
for n in range(1, 6):
    cubes.append(n ** 3)
print(cubes)
"""

# Assignment 55
# Question: From `[10,15,20,25,30]`, build list of values divisible by 10.
# Hint: if n % 10 == 0: append

"""
numbers = [10, 15, 20, 25, 30]
result = []
for n in numbers:
    if n % 10 == 0:
        result.append(n)
print(result)
"""

# Assignment 56
# Question: Compute sum of squares for integers 1 through 10.
# Hint: range(1, 11) and total += i**2

"""
total = 0
for i in range(1, 11):
    total += i ** 2
print(total)
"""

# Assignment 57
# Question: Print FizzBuzz for 1..20 (same rules).
# Hint: Check 15 first, then 3, then 5.

"""
for i in range(1, 21):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
"""

# Assignment 58
# Question: Print a left-aligned triangle of `*` with 5 rows.
# Hint: Row i has i stars; no leading spaces needed.

"""
for i in range(1, 6):
    print('*' * i)
"""

# Assignment 59
# Question: Search 1..10 for 8; if never found after loop, print `'Not in range'`. Use for-else.
# Hint: break when found; else clause if not.

"""
for i in range(1, 11):
    if i == 8:
        print('Found')
        break
else:
    print('Not in range')
"""

# Assignment 60
# Question: Find index of `'cherry'` in `fruits` list; print index or -1.
# Hint: Use enumerate and break on match.

"""
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    if fruit == 'cherry':
        print(i)
        break
else:
    print(-1)
"""

# Assignment 61
# Question: Compute average of `[10, 20, 30, 40, 50]`.
# Hint: sum / len after loop.

"""
values = [10, 20, 30, 40, 50]
print(sum(values) / len(values))
"""

# Assignment 62
# Question: Print pairs (i,j) where i and j are 1..3 and i <= j.
# Hint: Inner loop: range(i, 4) or if j >= i.

"""
for i in range(1, 4):
    for j in range(i, 4):
        print((i, j))
"""

# Assignment 63
# Question: Loop `points = [(0,0), (1,2), (3,4)]` and print distance from origin simplified as x+y.
# Hint: for x, y in points: print(x+y)

"""
points = [(0, 0), (1, 2), (3, 4)]
for x, y in points:
    print(x + y)
"""

# Assignment 64
# Question: Number lines of `lines = ['A','B','C']` starting at 1 using enumerate.
# Hint: enumerate(lines, start=1)

"""
lines = ['A', 'B', 'C']
for step, line in enumerate(lines, start=1):
    print(step, line)
"""

# Assignment 65
# Question: Print sequence 5, 10, 15, ..., 50 using range.
# Hint: range(5, 55, 5)

"""
for i in range(5, 51, 5):
    print(i, end=' ')
print()
"""

# Assignment 66
# Question: Sum digits of `n = 808` using a for loop over str(n).
# Hint: int(ch) for each character.

"""
n = 808
digit_sum = 0
for ch in str(n):
    digit_sum += int(ch)
print(digit_sum)
"""

# Assignment 67
# Question: Compute 6! using a for loop.
# Hint: fact = 1; multiply each i in range(1, 7).

"""
n = 6
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
"""

# Assignment 68
# Question: Check if 51 is prime using trial division in a for loop.
# Hint: Same pattern; 51 = 3 × 17.

"""
n = 51
is_prime = True
for d in range(2, int(n ** 0.5) + 1):
    if n % d == 0:
        is_prime = False
        break
print(is_prime)
"""

# Assignment 69
# Question: Print each element of `grid = [[9,8],[7,6]]` row by row.
# Hint: Nested for row in grid: for cell in row:

"""
grid = [[9, 8], [7, 6]]
for row in grid:
    for cell in row:
        print(cell)
"""

# Assignment 70
# Question: Count character frequencies in `'banana'` into a dict.
# Hint: for ch in 'banana': freq[ch] = freq.get(ch,0)+1

"""
word = 'banana'
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
"""