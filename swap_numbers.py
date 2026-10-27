number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("Before swapping: number1 =", number1, "number2 =", number2)
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print("After swapping: number1 =", number1, "number2 =", number2)