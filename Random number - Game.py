
import random

max_digit = input("Write the biggest number by you want to guess: ")

if int(max_digit) is False:
    print("Write a valid number above 0.")
elif int(max_digit) <= 0:
    print("Write a number above 0.")
else:
    max_digit = int(max_digit)
    
number = random.randint(0,max_digit)

number_of_guess = 0

while number_of_guess < 5:
    print('Guess a number between 0 and', max_digit,".")
    guess = input()
    guess = int(guess)
    number_of_guess += 1
    
    if number == guess:
        break
    elif number_of_guess == 5:
        break
    else:
        print("You guessed it wrong!")
        if guess > number:
            print("Guessed number is higher than the random number.")
        else:
            print("Guessed number is lower than the random number.")



if number == guess:
    print("Great, You guessed it right!")
elif number_of_guess >= 5:
    print("Unfortunately, Your chances are over.")

