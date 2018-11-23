print 'We are greeting You at our on-line grocery store!!! Choose Your items and we are going to calculate total price of Your bill! Have a nice day!'
shopping_list = []
print 
print 'Now You will see list of our good and prices for it and it\'s stock'
print
for key in prices:
  print key
  print 'Price is: %d per each' % (prices[key])
  print 'Stock is: %d' % (stock[key])
  print
print 'Now choose Your goods!'
for key in prices:
  new_list = raw_input('Enter Your items from the list: ')
  shopping_list.append(str(new_list))
  print 'We are putting %s in Your bag' % (new_list)

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] != 0:
      total += prices[item]
      print '%s is: %d' % (item, prices[item])
    else:
      print 'Sorry %s is out of stock' %(item)
      food.remove(item)
      print 'We\'ve removed this from your list: %s' % (food)
      total += prices[item]
  return total

print 'Your total price is: ' + str(compute_bill(shopping_list))