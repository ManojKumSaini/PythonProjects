#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

computer_wins = 0
user_wins = 0

options = ['rock','paper','scissors']

# rock is 0, paper is 1, scissors is 2 [Indexing]

while True:
    user_guess= input("Type Rock/Paper/Scissors or q to quit.: ").lower()
    
    if user_guess == 'q':
        break
    elif user_guess not in options:
        print("Please choose Rock/Paper/Scissors or q to quit.: ")
        continue
        
    computer_digit = random.randint(0,2)
    computer_guess = options[computer_digit]
    print("Computer choosed",computer_guess,".")
    
    if user_guess == 'rock' and computer_guess == 'scissors':
        print("You won.")
        user_wins += 1   
    elif user_guess == 'paper' and computer_guess == 'rock':
        print("You won.")
        user_wins += 1
    elif user_guess == 'scissors' and computer_guess == 'paper':
        print("You won.")
        user_wins += 1
    elif str(user_guess) == str(computer_guess):
        print("It's a tie, Let's try again.")
    else:
        print("Bad Luck!. You lost")
        computer_wins += 1
        
        
print("You won", user_wins, 'times.')        
print("Computer won", computer_wins, 'times.')
print("Thanks for playing this game.")