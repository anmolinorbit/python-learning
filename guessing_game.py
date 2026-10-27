import random
secret = random.randint(1,10)
guess = 0
while guess != secret :
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print("Congratulations! You guessed it right!")
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")        