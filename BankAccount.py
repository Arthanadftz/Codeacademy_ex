class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return '%s\'s acoount has balance: $%.2f' %(self.name, self.balance)
  def show_balance(self):
    print('Balance: $%.2f' %(self.balance))
  def deposit(self, amount):
    if amount <= 0:
      print('You have tried to deposit $%.2f. Deposit amount should be more then 0$.' %(amount))
      return
    else:
      print('$%.2f has been added to your account!' %(amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance:
      print('You can\'t withdrow $%.2f! This is less then your balance: $%.2f' %(amount, self.balance))
      return
    else:
      print('$%.2f has been removed from your account!' %(amount))
      self.balance -= amount
      self.show_balance()

def menu():
  print('Hello stranger! Please enter your name to get access to your account info.')
  name = raw_input('Enter your name: ')
  my_account = BankAccount(name)
  print(my_account)
  start = True
  while start:
    action = raw_input('Type B to see your balance. D for deposit and W for withdraw. E to exit: ')
    action = action.upper()
    if action == 'B':
      my_account.show_balance()
    elif action == 'D':
      amount = float(raw_input('How much do you want to deposit? Enter value: '))
      my_account.deposit(amount)
    elif action == 'W':
      amount = float(raw_input('How much do you want to withdraw? Enter value: '))
      my_account.withdraw(amount)
    elif action == 'E':
      print('Good bye %s.' %(name))
      start = False
    else:
      print('You have chosen invalid value. Try again')
      continue

menu()