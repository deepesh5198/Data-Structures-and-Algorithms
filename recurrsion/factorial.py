def factorial(n):
    """computes factorial of a positive integer"""
    if n == 0:                          #base case
        return 1

    else:                               #recursive case
        return n*factorial(n-1)

print(factorial(4))