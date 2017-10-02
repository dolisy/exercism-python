def rotate(string, num):
  alphabet_indexed = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z"
  }

  alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
  }

  import re
  string_re = re.compile(r"(\d|\D)")
  string_list = string_re.findall(string)

  rotated = []

  for char in string_list:
    if char.lower() in alphabet:
      index = alphabet[char.lower()] + num
      if index > 26:
        index = index - 26
      if char.lower() == char:
        rotated.append(alphabet_indexed[index])
      else:
        rotated.append(alphabet_indexed[index].upper())
    else:
      rotated.append(char)

  return "".join(rotated)


print rotate('OMG Z 1 2 34 hahaha!', 5)


















