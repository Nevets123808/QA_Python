def factorial(n):
    if n > 1: return n*factorial(n-1)
    return n

print(factorial(8))
print(factorial(5))
print(factorial(4))