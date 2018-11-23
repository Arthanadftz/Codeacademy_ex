#ABCD - DCBA:
def reverse(text):
  reverse = ''
  l = len(text) - 1
  while l >= 0:
    reverse += text[l]
    l -= 1
  return reverse

#Tests passed int is it even or not:
def is_even(x):
  if x % 2 == 0:
    return True
  return False

#Tests passed arg is int type or not:
import math
def is_int(x):
  if type(x) == int or x - math.ceil(x) == 0:
    return True
  return False

#Calculate factorial of passed int:
def factorial(x):
  total = 1
  for i in range(1, x + 1):
    total *= i
  return total
#Alternate Solution:
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total

#Calculate sum of all digits from passed int:
def digit_sum(n):
  total = 0
  string_n = str(n)
  for char in string_n:
    total += int(char)
  return total
#Alternate Solution:
def digit_sum(n):
  total = 0
  while n > 0:
    total += n % 10
    n = n // 10
  return total

#Tests passed int is prime or not:
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

#Replace vowel chars from string:
def anti_vowel(text):
  for char in text:
    if char in 'aeiouAEIOU':
      text = text.replace(char, '')
  return text

#Scrabble function
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  total = 0
  word = word.lower()
  for leter in word:
    for letter in score:
      if letter == leter:
        print '%s: %s' %(leter, score[letter])
        total += score[letter]
  print 'Your score is: %s' %(total)
  return total

scrabble_score('Python')

#Censor function(replace word from text on '*' * len(word):
def censor(text, word):
  res = ''
  words = text.split()
  count = 0
  stars = '*' * len(word)
  for i in words:
    if i == word:
      words[count] = stars
    count += 1
  res =' '.join(words)
  
  return res
  
print(censor("this hack is wack hack", "hack"))

#Count function
def count(sequence, item):
  count = 0
  for i in sequence:
    if i == item:
      count += 1
  return count
print count([1, 2, 1, 1], 1)

#Purify list from odd numbers:
def purify(lst):
  lst_res = []
  for i in lst:
    if i % 2 == 0:
      lst_res.append(i)
  return lst_res

#Product function:
def product(lst):
  res = 1
  for i in lst:
    res *= i
  return res

print product([4, 5, 5])

#Remove duplicates from list(return new list, not modify input):
def remove_duplicates(inp_lst):
  if inp_lst == []:
    return []
  inp_lst = sorted(inp_lst)
  out_lst = [inp_lst[0]]
  for i in inp_lst:
    if i > out_lst[-1]:
      out_lst.append(i)
  return out_lst

#Median function:
def median(lst):
  lst = sorted(lst)
  res = 0
  if len(lst)%2 == 0:
    res = float(lst[len(lst)/2 - 1] + lst[len(lst)/2])/2
  else:
    res = lst[len(lst)/2]
  return res

 #Sum, avg, variance, deviation, functions for lists:
 grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  variance /= len(scores)
  return variance

variance = grades_variance(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

