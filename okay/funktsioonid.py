# 1
def arithmetic():
    operation = input("Enter Symbol: ")  
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Sisesta kehtiv sümbol"  

# 2
def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 3
import math
def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal

# 4
def season(month):
    if month in [12, 1, 2]:
        return "talv"
    elif month in [3, 4, 5]:
        return "kevad"
    elif month in [6, 7, 8]:
        return "suvi"
    elif month in [9, 10, 11]:
        return "sügis"
    else:
        return "Vale kuu number"

# 5
def bank(a, years):
    total = a
    for _ in range(years):
        total *= 1.10  
    return total

# 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} jagajad: {i} ja {n//i}")
            return False
    return True

# 7
def date(day, month, year):
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return day <= 31
    elif month in [4, 6, 9, 11]:
        return day <= 30
    elif month == 2:
        if is_year_leap(year):
            return day <= 29
        else:
            return day <= 28
    return False

# 8
def XOR_cipher(text, key):
    return ''.join([chr(ord(c) ^ ord(key)) for c in text])

def XOR_uncipher(cipher_text, key):
    return ''.join([chr(ord(c) ^ ord(key)) for c in cipher_text])

# 9
def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# 10
def min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

# 11
def unique_elements(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
