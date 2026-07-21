# =========================
# If / Else Assignments
# =========================

# Assignment 1
# Question: Ask whether a variable `score` is at least 50. If so, print `'Pass'`.
# Hint: Use `if score >= 50:` and one indented print line.

"""
score = 50
if score >= 50:
    print('Pass')
"""

# Assignment 2
# Question: Set `n = 14`. Print `'even'` if `n` is even, otherwise print `'odd'`.
# Hint: Modulo: `n % 2 == 0` means even.

"""
n = 14
if n % 2 == 0:
    print('even')
else:
    print('odd')
"""

# Assignment 3
# Question: Given `temp = 38`, print `'Hot'` if temp > 35, `'Warm'` if temp > 25, else `'Cool'`.
# Hint: Chain three branches with if / elif / else.

"""
temp = 38
if temp > 35:
    print('Hot')
elif temp > 25:
    print('Warm')
else:
    print('Cool')
"""

# Assignment 4
# Question: Compare `x = 8` and `y = 12`. Print which variable holds the larger value.
# Hint: Use a single if-else with `x > y`.

"""
x, y = 8, 12
if x > y:
    print(x)
else:
    print(y)
"""

# Assignment 5
# Question: If `language == 'Python'`, print `'Great choice!'`, else print `'Try Python!'`.
# Hint: String comparison is case-sensitive.

"""
language = 'Python'
if language == 'Python':
    print('Great choice!')
else:
    print('Try Python!')
"""

# Assignment 6
# Question: If `status != 'active'`, print `'Account inactive'`.
# Hint: Single-line if is enough.

"""
status = 'inactive'
if status != 'active':
    print('Account inactive')
"""

# Assignment 7
# Question: Print `'Valid'` if `hour` is between 9 and 17 inclusive, else `'Invalid'`.
# Hint: Use `9 <= hour <= 17` or `and`.

"""
hour = 10
if 9 <= hour <= 17:
    print('Valid')
else:
    print('Invalid')
"""

# Assignment 8
# Question: Grant access only if `logged_in` and `is_premium` are both True. Print `'Access OK'` or `'Denied'`.
# Hint: Both must be True.

"""
logged_in = True
is_premium = True
if logged_in and is_premium:
    print('Access OK')
else:
    print('Denied')
"""

# Assignment 9
# Question: Print `'Holiday'` if `month` is `'December'` OR `'July'`, else `'Regular month'`.
# Hint: Use `or` between two equality checks.

"""
month = 'December'
if month == 'December' or month == 'July':
    print('Holiday')
else:
    print('Regular month')
"""

# Assignment 10
# Question: If `is_locked` is False, print `'Door is open'`. Use `not`.
# Hint: `not is_locked` is the idiomatic test.

"""
is_locked = False
if not is_locked:
    print('Door is open')
"""

# Assignment 11
# Question: Check if `score` is strictly between 0 and 100: print `'In range'` or `'Out of range'`.
# Hint: Use `0 < score < 100`.

"""
score = 42
if 0 < score < 100:
    print('In range')
else:
    print('Out of range')
"""

# Assignment 12
# Question: If `'@'` is in string `email`, print `'Valid format hint'`, else `'Missing @'`.
# Hint: Use `in` on the string.

"""
email = 'user@example.com'
if '@' in email:
    print('Valid format hint')
else:
    print('Missing @')
"""

# Assignment 13
# Question: Accept `'y'`, `'Y'`, `'yes'`, or `'YES'` as confirmation using `.lower()`.
# Hint: Store normalized input: `ans = response.lower()`.

"""
response = 'Y'
ans = response.lower()
if ans in ('y', 'yes'):
    print('Confirmed')
else:
    print('Not confirmed')
"""

# Assignment 14
# Question: If `balance >= 100`, check nested: if `pin_correct`, print `'Withdraw OK'`, else `'Wrong PIN'`.
# Hint: Outer if on balance; inner if on pin.

"""
balance = 150
pin_correct = True
if balance >= 100:
    if pin_correct:
        print('Withdraw OK')
    else:
        print('Wrong PIN')
else:
    print('Insufficient balance')
"""

# Assignment 15
# Question: Map `size` ('S','M','L') to prices 10, 15, 20 with elif; print the price.
# Hint: Four branches including default.

"""
size = 'M'
if size == 'S':
    price = 10
elif size == 'M':
    price = 15
elif size == 'L':
    price = 20
else:
    price = 0
print(price)
"""

# Assignment 16
# Question: Use `is_admin` directly in an if to print `'Admin panel'` or `'User panel'`.
# Hint: Avoid `== True`; write `if is_admin:`.

"""
is_admin = True
if is_admin:
    print('Admin panel')
else:
    print('User panel')
"""

# Assignment 17
# Question: Set `label` to `'Even'` or `'Odd'` in one line using `n = 9`.
# Hint: Ternary: `'Even' if n % 2 == 0 else 'Odd'`.

"""
n = 9
label = 'Even' if n % 2 == 0 else 'Odd'
print(label)
"""

# Assignment 18
# Question: If list `items` is empty (falsy), print `'Cart empty'`, else `'Cart has items'`.
# Hint: Use `if items:` — empty list is falsy.

"""
items = []
if items:
    print('Cart has items')
else:
    print('Cart empty')
"""

# Assignment 19
# Question: Print `'Data found'` if dict `cache` is non-empty, else `'No cache'`.
# Hint: `if cache:` tests non-empty dict.

"""
cache = {'a': 1}
if cache:
    print('Data found')
else:
    print('No cache')
"""

# Assignment 20
# Question: Require `len(password) >= 8` AND `any(c.isdigit() for c in password)`. Print pass/fail.
# Hint: Combine with `and`.

"""
password = 'abc12345'
if len(password) >= 8 and any(c.isdigit() for c in password):
    print('pass')
else:
    print('fail')
"""

# Assignment 21
# Question: Categorize `wind_kmh`: Calm (<10), Breezy (<25), Windy (>=25).
# Hint: Two elif plus final else.

"""
wind_kmh = 30
if wind_kmh < 10:
    print('Calm')
elif wind_kmh < 25:
    print('Breezy')
else:
    print('Windy')
"""

# Assignment 22
# Question: Given `plan` in `'free'`, `'pro'`, `'enterprise'`, print storage limits 1GB, 10GB, 100GB.
# Hint: Use elif for each plan.

"""
plan = 'pro'
if plan == 'free':
    print('1GB')
elif plan == 'pro':
    print('10GB')
elif plan == 'enterprise':
    print('100GB')
"""

# Assignment 23
# Question: Orders: >=500 → 25% off, >=200 → 15%, else 0%. Compute final price for `amount=350`.
# Hint: Multiply by `(1 - discount)`.

"""
amount = 350
discount = 0.0
if amount >= 500:
    discount = 0.25
elif amount >= 200:
    discount = 0.15
final_price = amount * (1 - discount)
print(final_price)
"""

# Assignment 24
# Question: Check if `year = 1900` is a leap year using the same rule. Print result.
# Hint: 1900 is divisible by 100 but not 400.

"""
year = 1900
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Leap year')
else:
    print('Not a leap year')
"""

# Assignment 25
# Question: For `ch = 'M'`, print whether it is a vowel or consonant (case-insensitive).
# Hint: Use `.lower()` and `in 'aeiou'`.

"""
ch = 'M'
if ch.lower() in 'aeiou':
    print('Vowel')
else:
    print('Consonant')
"""

# Assignment 26
# Question: Classify `value = 0` as `'positive'`, `'negative'`, or `'zero'`.
# Hint: Three mutually exclusive branches.

"""
value = 0
if value > 0:
    print('positive')
elif value < 0:
    print('negative')
else:
    print('zero')
"""

# Assignment 27
# Question: Print `'Weekend'` if `day` is `'Saturday'` or `'Sunday'`, else `'Weekday'`.
# Hint: `day in ('Saturday', 'Sunday')`.

"""
day = 'Saturday'
if day in ('Saturday', 'Sunday'):
    print('Weekend')
else:
    print('Weekday')
"""

# Assignment 28
# Question: For `bmi = 27.5`, assign category using standard thresholds and print it.
# Hint: Same breakpoints as the example.

"""
bmi = 27.5
if bmi < 18.5:
    category = 'Underweight'
elif bmi < 25:
    category = 'Normal'
elif bmi < 30:
    category = 'Overweight'
else:
    category = 'Obese'
print(category)
"""

# Assignment 29
# Question: Approve if `age >= 21` and nested `savings >= 5000`; else print specific rejection.
# Hint: Nested if-else with clear messages.

"""
age = 25
savings = 6000
if age >= 21:
    if savings >= 5000:
        print('Approved')
    else:
        print('Savings too low')
else:
    print('Too young')
"""

# Assignment 30
# Question: Map choices `'A'`,`'B'`,`'C'` to `'Add'`,`'Browse'`,`'Checkout'`. Handle invalid.
# Hint: elif per letter; else for unknown.

"""
choice = 'B'
if choice == 'A':
    print('Add')
elif choice == 'B':
    print('Browse')
elif choice == 'C':
    print('Checkout')
else:
    print('Invalid')
"""

# Assignment 31
# Question: Discount if (`items >= 3` and `member`) OR `coupon == 'SAVE10'`. Print result.
# Hint: Parentheses clarify grouping.

"""
items = 4
member = True
coupon = 'SAVE10'
if (items >= 3 and member) or coupon == 'SAVE10':
    print('Discount')
else:
    print('No discount')
"""

# Assignment 32
# Question: If variable `middle_name` is `None`, print `'N/A'`, else print the name.
# Hint: Use `is None` / `is not None`.

"""
middle_name = None
if middle_name is None:
    print('N/A')
else:
    print(middle_name)
"""

# Assignment 33
# Question: If `data` is a `list`, print its length; elif `dict`, print key count; else `'Unknown'`.
# Hint: Use isinstance for list and dict.

"""
data = [1, 2, 3]
if isinstance(data, list):
    print(len(data))
elif isinstance(data, dict):
    print(len(data))
else:
    print('Unknown')
"""

# Assignment 34
# Question: Postage: <=0.5kg → $3, <=2kg → $7, else $15. Compute for `weight_kg = 1.8`.
# Hint: Ordered elif from smallest tier.

"""
weight_kg = 1.8
if weight_kg <= 0.5:
    cost = 3
elif weight_kg <= 2:
    cost = 7
else:
    cost = 15
print(cost)
"""

# Assignment 35
# Question: Weekday: adult $12, child $6. Weekend: adult $18, child $10. Set flags and print price.
# Hint: Nested if on `is_weekend` then `age < 12`.

"""
is_weekend = False
age = 10
if is_weekend:
    if age < 12:
        price = 10
    else:
        price = 18
else:
    if age < 12:
        price = 6
    else:
        price = 12
print(price)
"""