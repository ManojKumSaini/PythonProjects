import random
import time
Name = input("May I have your name please?: ")

print(f"Hello {Name}! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(2)

print("Picking a number...")
time.sleep(2)

guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guesses = 1

while guess != correct_number:
    guesses += 1
    
    if guess > correct_number:
        if guess - correct_number < 5:
            guess = int(input("You are going good. Just try a little lower. Have a guess now?: "))
        else:
            guess = int(input("Nope! Please guess a lower number. Try Now: "))
    if guess < correct_number:
        if correct_number - guess < 5:
            guess = int(input("Ah! You are close to the number. Just try a little higher. Have your guess now?: "))
        else:
            guess = int(input("Wrong! You need to guess higher. What is your guess?: "))
    
print(f"Congrats {Name}!, You guessed it correct. It took {guesses} guesses.")    
