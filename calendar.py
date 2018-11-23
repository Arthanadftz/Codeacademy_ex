"""This is calender witch gives can view all the data, add/delete/update events from it by your comand"""
from time import sleep, strftime

USER_FIRST_NAME = 'Nikita'
calendar = {}
def welcome():
  print('Welcome, %s.' %(USER_FIRST_NAME))
  print('Calendar starting...')
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")  
  print("Current time: " + strftime('%H:%M:%S'))
  sleep(1)
  print('What would you like to do?')
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print('Sorry:( Your calendar is empty...')
      else:
        print(calendar)
    elif user_choice == 'U':
      date = raw_input('What date?')
      if date in calendar.keys():
        print('Aww! It seems like you are trying to rewrite existing even: %s.' %(calendar[date]))
        sure = raw_input('Are you sure? Y for Yes N otherwise: ')
        sure = sure.upper()
        if sure == 'Y':
          update = raw_input('Enter the update: ')
          calendar[date] = update
          print('Calendar succesfully updated with %s at %s' %(update, date))
          print(calendar)
        else:
          continue
      else:
          update = raw_input('Enter the update: ')
          calendar[date] = update
          print('Calendar succesfully updated with %s at %s' %(update, date))
          print(calendar)
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input('Enter date (MM/DD/YYYY)')
      if (len(date) != 10 or int(date[6:]) < int(strftime("%Y"))):
        print('Invalid date format')
        try_again = raw_input('Try Again? Y for Yes, N for No: ')
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print('Calendar succesfully updated with added %s at %s' %(event, date))
        print(calendar)
    elif user_choice == 'D':
      if len(calendar.keys()) < 0:
        print('Calendar is empty! There is nothing to delete yet.')
      elif len(calendar.keys()) > 0:
        event = raw_input('What event?')
        for date in calendar.keys():
          if event == calendar[date]:
            sure = raw_input('Are you sure to delete %s event? Y for Yes, N otherwise.' %(event))
            sure = sure.upper()
            if sure == 'Y':
              del calendar[date]
              print('Event %s succesfully deleted from calender' %(event))
              print(calendar)
              break
          else:    
            print('Yo\'ve entered incorrect event')
            start = False
      else:
        continue 
    elif user_choice == 'X':
      sure = raw_input('You are trying to exit app. Are you sure? Y for Yes, N for No: ')
      sure = sure.upper()
      if sure == 'Y':
        start = False
      else:
        continue
    else:
      print('You have entered an invalid command.')
      start = False
      
start_calendar()