"""Try to guess a number that system randomly select. Test your luck!"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input('Guess the number: '))
  return guess

def roll_dise(number_of_sides=6):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print('The maximum possible value is: %d' %(max_val))
  guess = get_user_guess()
  if guess > max_val:
    print('Your value is %d and it\'s more than %d' %(guess, max_val))
    print('Roll again')
    roll_dise()
  elif guess < 2:
    print('Your value is %d and it\'s less than possible 2' %(guess))
    print('Roll again')
    roll_dise()
  else:
    print('Rolling...')
    sleep(2)
    print('First roll is: %d' %(first_roll))
    sleep(1)
    print('Second roll is: %d' %(second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print('Result is: %d' %(total_roll))
    sleep(1)
    if guess == total_roll:
      print('You won!')
    else:
      print('You lose.')
      print('Try again.')
      roll_dise()   
roll_dise(6)