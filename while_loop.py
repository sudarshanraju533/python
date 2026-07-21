# =========================
# While Loop Assignments
# =========================

# Assignment 71
# Question: Print numbers 10 down to 1 using while (decrement each step).
# Hint: Start count=10; while count >= 1: print; count -= 1

"""
count = 10
while count >= 1:
    print(count, end=' ')
    count -= 1
print()
"""

# Assignment 72
# Question: Simulate up to 3 guesses of secret `4` with guesses [2,4]. Print win or lose.
# Hint: while guess != secret and attempts < 3

"""
secret = 4
guess = 0
attempts = 0
while guess != secret and attempts < 3:
    guess = [2, 4][attempts]
    attempts += 1
    print(f'Attempt {attempts}: {guess}')
print('Win' if guess == secret else 'Lose')
"""

# Assignment 73
# Question: Double `x` starting at 1 until `x > 100`; print final x and break.
# Hint: while True with if x > 100: break; x *= 2

"""
x = 1
while True:
    if x > 100:
        print(x)
        break
    x *= 2
"""

# Assignment 74
# Question: Print multiples of 5 between 1 and 50 using while + continue for non-multiples.
# Hint: Increment n; if n % 5 != 0: continue

"""
n = 1
while n <= 50:
    if n % 5 != 0:
        n += 1
        continue
    print(n, end=' ')
    n += 1
print()
"""

# Assignment 75
# Question: Read from `nums = [3,1,4,0,9]` until 0; sum values before sentinel.
# Hint: Same sentinel break pattern.

"""
nums = [3, 1, 4, 0, 9]
total = 0
for value in nums:
    if value == 0:
        break
    total += value
print(total)
"""

# Assignment 76
# Question: Add 1+2+3+… until sum exceeds 100; print how many terms were added.
# Hint: while total <= 100: accumulate

"""
total = 0
terms = 0
while total <= 100:
    terms += 1
    total += terms
print(terms)
"""

# Assignment 77
# Question: Count down from 5 to 1, printing each number, then `'Go!'`.
# Hint: while t > 0: print; decrement

"""
t = 5
while t > 0:
    print(t)
    t -= 1
print('Go!')
"""

# Assignment 78
# Question: Count positive numbers in `[5,3,0,-2]` stopped at first non-positive.
# Hint: while index in range and value > 0

"""
values = [5, 3, 0, -2]
count = 0
index = 0
while index < len(values) and values[index] > 0:
    count += 1
    index += 1
print(count)
"""

# Assignment 79
# Question: Print `'Hello'` once, then ask if `repeat` is False to stop; else repeat (max 3).
# Hint: Use while True and break when done.

"""
repeat = True
count = 0
while True:
    print('Hello')
    count += 1
    if count >= 3 or not repeat:
        break
"""

# Assignment 80
# Question: Allow 3 attempts to match `pin = '1234'` with simulated inputs; print outcome.
# Hint: while entered != pin and attempts < 3

"""
pin = '1234'
entered = ''
attempts = 0
while entered != pin and attempts < 3:
    entered = ['0000', '1111', '1234'][attempts]
    attempts += 1
    print(f'Try {attempts}: {entered}')
print('Matched' if entered == pin else 'Failed')
"""

# Assignment 81
# Question: Simulate menu picking `'a'`,`'b'`,`'q'` until `'q'` breaks loop.
# Hint: while True; break on quit.

"""
while True:
    choice = input('Enter a, b, or q: ')
    if choice == 'q':
        print('Quit')
        break
    elif choice == 'a':
        print('Option A')
    elif choice == 'b':
        print('Option B')
"""

# Assignment 82
# Question: Print Collatz sequence starting at `n = 10` until 1.
# Hint: Same even/odd rules in while n != 1.

"""
n = 10
sequence = [n]
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    sequence.append(n)
print(sequence)
"""

# Assignment 83
# Question: Print Fibonacci numbers less than 200 using while.
# Hint: Same swap: a, b = b, a+b while b < 200

"""
a, b = 0, 1
while b < 200:
    print(b, end=' ')
    a, b = b, a + b
print()
"""

# Assignment 84
# Question: Find GCD of 270 and 192 using Euclidean while loop.
# Hint: while b: a, b = b, a % b

"""
a, b = 270, 192
while b:
    a, b = b, a % b
print(a)
"""

# Assignment 85
# Question: Reverse integer `n = 908` using while and modulo arithmetic.
# Hint: reversed = reversed*10 + n%10; n//=10

"""
n = 908
reversed_num = 0
while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n //= 10
print(reversed_num)
"""

# Assignment 86
# Question: Factorize 84 into primes using nested while.
# Hint: Outer while d*d<=temp; inner while temp%d==0.

"""
n = 84
factors = []
d = 2
temp = n
while d * d <= temp:
    while temp % d == 0:
        factors.append(d)
        temp //= d
    d += 1
if temp > 1:
    factors.append(temp)
print(factors)
"""

# Assignment 87
# Question: Print 4×4 grid of `'.'` characters using nested while.
# Hint: row 0..3, col 0..3, print dot without newline inner.

"""
row = 0
while row < 4:
    col = 0
    while col < 4:
        print('.', end='')
        col += 1
    print()
    row += 1
"""

# Assignment 88
# Question: Search for 7 in `[1,3,5,9]` with while; use else to print `'Missing'`.
# Hint: while i < len; break on match; else: Missing

"""
nums = [1, 3, 5, 9]
i = 0
while i < len(nums):
    if nums[i] == 7:
        print('Found')
        break
    i += 1
else:
    print('Missing')
"""

# Assignment 89
# Question: Process `cmds = ['a','b','stop']` until `'stop'` with while True.
# Hint: break when cmd == 'stop'.

"""
cmds = ['a', 'b', 'stop']
for cmd in cmds:
    print(cmd)
    if cmd == 'stop':
        break
"""

# Assignment 90
# Question: Make 83 cents with greedy coins [25,10,5,1]; print coin count.
# Hint: for each coin: while amount >= coin: subtract

"""
amount = 83
coins = [25, 10, 5, 1]
count = 0
for coin in coins:
    while amount >= coin:
        amount -= coin
        count += 1
print(count)
"""

# Assignment 91
# Question: Binary-search target `23` in sorted list above; print index.
# Hint: while lo <= hi: compute mid, adjust lo/hi.

"""
arr = [2, 5, 8, 12, 16, 23, 38]
target = 23
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
"""

# Assignment 92
# Question: Average `[4,8,12,0]` values before sentinel 0 using while.
# Hint: Break on 0; track sum and count.

"""
stream = [4, 8, 12, 0]
total = 0
count = 0
for value in stream:
    if value == 0:
        break
    total += value
    count += 1
print(total / count if count else 0)
"""

# Assignment 93
# Question: Find LCM of 9 and 12 using incrementing while.
# Hint: Start at max(a,b); while not divisible by both: lcm += 1

"""
a, b = 9, 12
lcm = max(a, b)
while lcm % a != 0 or lcm % b != 0:
    lcm += 1
print(lcm)
"""

# Assignment 94
# Question: Check if `'level'` is palindrome using two-pointer while.
# Hint: left/right converge; break on mismatch.

"""
s = 'level'
left, right = 0, len(s) - 1
is_palindrome = True
while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print(is_palindrome)
"""

# Assignment 95
# Question: Compute 3**4 with a while loop (no ** operator).
# Hint: result = 1; while count < 4: result *= 3

"""
base, exp = 3, 4
result = 1
count = 0
while count < exp:
    result *= base
    count += 1
print(result)
"""

# Assignment 96
# Question: Simulate stack pop from `[1,2,3]` using while and pop().
# Hint: while stack: print(stack.pop())

"""
stack = [1, 2, 3]
while stack:
    print(stack.pop())
"""

# Assignment 97
# Question: Simulate searching secret 20 in 1..50 with guesses [25,12,20].
# Hint: Adjust bounds; break when equal.

"""
secret = 20
low, high = 1, 50
guesses = [25, 12, 20]
for guess in guesses:
    if guess == secret:
        print('Found')
        break
    elif guess < secret:
        low = guess + 1
    else:
        high = guess - 1
else:
    print('Not found')
"""

# Assignment 98
# Question: Use `active = True` flag; decrement `tries` from 3 to 0 then set active False.
# Hint: while active: ... if tries == 0: active = False

"""
active = True
tries = 3
while active:
    print(tries)
    tries -= 1
    if tries == 0:
        active = False
"""

# Assignment 99
# Question: Print inverted pyramid of numbers (4 rows) using nested while.
# Hint: Outer row 4..1; inner prints row times.

"""
row = 4
while row >= 1:
    col = 1
    while col <= row:
        print(row, end='')
        col += 1
    print()
    row -= 1
"""

# Assignment 100
# Question: Build a while loop reading simulated inputs until `'done'`; if numeric, square it and print.
# Hint: while True; if val == 'done': break; elif val.isdigit(): print(int(val)**2)

"""
values = ['2', '4', 'done', '6']
for val in values:
    if val == 'done':
        print('Done')
        break
    elif val.isdigit():
        print(int(val) ** 2)
"""