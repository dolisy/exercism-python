class Allergies(object):

  def __init__(self, number):
    self.number = number
    self.allergies_list = {
      1: "eggs",
      2: "peanuts",
      4: "shellfish",
      8: "strawberries",
      16: "tomatoes",
      32: "chocolate",
      64: "pollen",
      128: "cats"
    }

  def is_allergic_to(self, string):
    if string in self.lst:
      return True
    else:
      return False


  @property
  def lst(self):
    value = self.number
    count = 0
    allergy_values = []
    if self.number == 0:
      return []
    else:
      while True:
        while True:
          rest = value - 2 ** count
          if rest >= 0:
            count += 1
          else:
            break
        allergy_values.append(int(2 ** (count - 1)))
        if value == 2 ** (count - 1):
          break
        else:
          value = value - 2 ** (count - 1)
          count = 0
      lst = []
      for allergy_value in allergy_values:
        if allergy_value in self.allergies_list.keys():
          lst.append(self.allergies_list[allergy_value])
      return lst



























