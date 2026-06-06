import random



secretnumber = random.randint(1, 100)

attempts = 0
guess = 0
while secretnumber != guess:
    guess = int(input("enter a number between 1-100: "))
    attempts += 1
    if secretnumber > guess:
        print("the number is higher")
    elif secretnumber < guess:
        print("the number is lesser")
    else:
        print(f"yay you guess right in {attempts} attempts")