import random

secret = random.randint(1,10)
guess = int(input("Guess a number between 1 to 10: "))
print(secret)

if guess == secret :
    print("You guessed it right!")
elif guess < secret :
    print("you guessed it wrong! the number is greater than your guess.")
else:
    print("you guessed it wrong! the number is less than your guess.")        