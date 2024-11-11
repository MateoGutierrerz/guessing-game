import random
import time
import math

print("Guess a number 1 out of 100, you get six tries")
random_number = random.randint(1, 100)
input1 = int(input("Guess 1: "))
if input1 == random_number:
    print(f"You Won! The number was {random_number}")
elif input1 < random_number:
        print("Too low")
else:
        print("Too High")
input2 = int(input("Guess 2: "))
if input2 == random_number:
    print(f"You Won! The number was {random_number}")
elif input2 < random_number:
        print("Too low")
else:
        print("Too High")
input3 = int(input("Guess 3: "))
if input3 == random_number:
    print(f"You Won! The number was {random_number}")
elif input3 < random_number:
        print("Too low")
else:
        print("Too High")
input4 = int(input("Guess 4: "))
if input4 == random_number:
    print(f"You Won! The number was {random_number}")
elif input4 < random_number:
        print("Too low")
else:
        print("Too High")
input5 = int(input("Guess 5: "))
if input5 == random_number:
    print(f"You Won! The number was {random_number}")
elif input5 < random_number:
        print("Too low")
else:
        print("Too High")
input6 = int(input("Guess 6: "))
if input6 == random_number:
    print(f"You Won! The number was {random_number}")
elif input6 < random_number:
        print("You Lost")
else:
        print("You Lost")
