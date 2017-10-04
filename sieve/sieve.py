def sieve(limit):
  if limit >= 2:
    numbers = [x for x in range(2,limit + 1)]
    prime = 2
    sieve = []

    while True:
      for number in numbers:
        if number % prime == 0:
          numbers.remove(number)
      sieve.append(prime)
      if numbers != []:
        prime = numbers[0]
      else:
        break
    return sieve
  else:
    return []
