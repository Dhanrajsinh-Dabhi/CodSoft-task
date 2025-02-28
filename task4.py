# import tkinter as tk

import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        print("Let's play Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose: ", user_choice)
        print("Computer chose: ", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        print("you want to play again?<yes/no>")
        ch=input("enter your choise: ").lower()
        if ch != "yes":
            break


       


play_game()






