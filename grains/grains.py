import numpy as np

def on_square(integer_number):
  if integer_number in range(1, 65):
    return pow(2, integer_number - 1)
  else:
    raise ValueError

def total_after(integer_number):
  if integer_number in range(1, 65):
    a = [pow(2, x) for x in range(0, integer_number)]
    return sum(a)
  else:
    raise ValueError
