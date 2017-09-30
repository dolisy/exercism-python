def is_isogram(string):
  isogram = True

  alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
  ]

  letters = []

  for letter in string:
    if letter.lower() in letters:
      isogram = False
    elif letter.lower() in alphabet:
      letters.append(letter.lower())
  return isogram

# # test function
# print is_isogram("isogram")
# print is_isogram("Isogram")
# print is_isogram("isograms")
# print is_isogram("isogramS")
# print is_isogram("isog-ram")
# print is_isogram("Is-ogr-am")
# print is_isogram("isogra-ms")
# print is_isogram("is-ogram-S")




