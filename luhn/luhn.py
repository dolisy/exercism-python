import re

class Luhn(object):
  def __init__(self, string):
    self.numbers = string.replace(' ', '')

  def is_valid(self):
    if len(self.numbers) < 2:
      return False
    try:
        return (
          sum([int(x) for i, x in enumerate(str(self.numbers)) if (len(str(self.numbers)) - i) % 2 == 1])
          +
          sum([2 * int(x) for i, x in enumerate(str(self.numbers)) if (len(str(self.numbers)) - i) % 2 == 0 and 2 * int(x) <= 9])
          +
          sum([2 * int(x) - 9 for i, x in enumerate(str(self.numbers)) if (len(str(self.numbers)) - i) % 2 == 0 and 2 * int(x) > 9])

        ) % 10 == 0
    except ValueError:
      return False
