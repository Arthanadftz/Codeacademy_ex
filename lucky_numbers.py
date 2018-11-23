from random import randint

random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess not in range(11):
    print "You have entered %s! Please, enter number from 0 to 10 inclusive" %(guess)
  else:
    if guess == random_number:
      print "You win!"
      break
    guesses_left -= 1
    print "You have entered %s. Unfortunately it's wrong:( Try again." %(guess)
else:
  print "You lose"