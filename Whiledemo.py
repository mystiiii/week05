import random

magic = random.randint(1, 100)

ans = int(input("Guess a number between 1 and 100: "))
while ans != magic:
    if ans > magic:
        print("You guessed too high!")
    elif ans < magic:
        print("You guessed too low!")
    ans = int(input("Guess a number between 1 and 100: "))
else:
    print("You guessed correct!")