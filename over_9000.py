def over_nine_thousand(lst):
  i = 0
  total = 0
  if len(lst) < 1:
    return 0
  while total <= 9000 and i < len(lst):
    total += lst[i]
    i += 1
  return total
		
print(over_nine_thousand([8000, 900, 120, 5000]))

def over_nine_thousand_f(lst):
  total = 0
  if len(lst) < 1:
    return 0
  for i in lst:
    if total > 9000:
      break
    else:
      total += i
  return total

print(over_nine_thousand_f([8000, 900, 120, 5000]))