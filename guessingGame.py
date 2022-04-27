import random
number = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("Enter the number between 1-9:"))
    if(guess > number):
        print("Your guess is too large")
    elif(guess == number):
        print("Congratulations! YOU WON!!")
        break
    else:
        print("Your number is too less")
    chances = chances + 1
if not chances > 5:
    print("YOU LOSE!!! The number is", number)
