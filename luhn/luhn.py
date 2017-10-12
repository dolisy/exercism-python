import re

class Luhn(object):
  def __init__(self, string):
    self.string = string

  def is_valid(self):
    regex = ur"\d"
    numbers = re.findall(regex, self.string)

    result = [int(x) * (2 - (i%2)) for i, x in enumerate(numbers)]

    if sum(result) > 0:
      return sum(result) % 10 == 0
    else:
      return False
