def sum_of_multiples(n, multiples):
  numbers = [x for x in range(0,n)]
  sum_of_multiples = 0
  for number in numbers:
    value = False
    for multiple in multiples:
      if number % multiple == 0:
        value = True
    if value == True:
      sum_of_multiples += number
  return sum_of_multiples

