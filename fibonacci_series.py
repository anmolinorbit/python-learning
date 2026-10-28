number = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1
for _ in range(number):
    print(a, end=" ")
    a, b = b, a + b
    