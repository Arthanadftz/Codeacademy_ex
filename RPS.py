"""Let's play RPS?! You will show your tool and I'll do the same! Then program will compare who have won. Good luck!"""
from random import randint

options = ['ROCK', 'PAPER', 'SCISSORS']
message = {
  'tie': 'Yawn it\'s a tie!',
  'won': 'Yay you won!',
  'lost': 'Aww you lost!'
}

def decide_winner(user_choice, computer_choice):
  print(str(user_choice))
  print(str(computer_choice))
  if user_choice == computer_choice:
    print(message['tie'])
  elif user_choice == options[0] and computer_choice == options[2] or user_choice == options[1] and computer_choice == options[0] or user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print(message['lost'])
    x = raw_input("Again?Type 'Y' or 'N'.")
    x = x.upper()
    if x == 'Y':
      play_RPS()

def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)

play_RPS()