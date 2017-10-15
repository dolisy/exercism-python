def prime_factors(natural_number):
  prime_factors = [];
  i = 2
  while natural_number > 1:
    if natural_number % i == 0:
      prime_factors.append(i)
      natural_number = natural_number / i
    else:
      i += 1
  return prime_factors
