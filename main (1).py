def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


# Example usage:
number = 5  # You can change this to any positive integer
result = factorial(number)
print(f"The factorial of {number} is {result}")
