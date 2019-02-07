import random

answer = input("Roll? (yes/no)")

if answer.lower().strip() == "yes":
    value = random.randint(1,6)
    print(value)