import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # potential ZeroDivisionError

def power(base, exp):
    if exp < 0:
        return 1 / power(base, -exp)
    result = 1
    for i in range(exp):
        result = result * base
    return result

def factorial(n):
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  # inefficient: should stop at sqrt(n)
        if n % i == 0:
            return False
    return True

def stats(numbers):
    total = 0
    for n in numbers:
        total = total + n
    avg = total / len(numbers)  # ZeroDivisionError if empty list
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return {"sum": total, "avg": avg, "variance": variance, "std": math.sqrt(variance)}

if __name__ == "__main__":
    print(add(1, 2))
    print(divide(10, 2))
    print(factorial(5))
    print(stats([1, 2, 3, 4, 5]))
