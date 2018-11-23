def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]
  print("Input list: \n%s\n\nMaximum value is : %s\n\nMax exponent is: %s\n" %(to_be_sorted, maximum_value, max_exponent))

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position
    print("For iteration %s, position index is: (%s)"%(exponent + 1, index))

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      try:
        digit = number_as_a_string[index]
        digit = int(digit)
      except IndexError:
        digit = 0

      digits[digit].append(number)
    print(digits)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]

print("Sorted list: \n%s\n"%(radix_sort(unsorted_list)))