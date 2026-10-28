def fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial
result = fact(int(input("Enter a number: ")))
print(result)    