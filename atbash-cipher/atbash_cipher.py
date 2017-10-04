def encode(string):
  plain = "abcdefghijklmnopqrstuvwxyz123456789"
  cipher = "zyxwvutsrqponmlkjihgfedcba123456789"

  code = ""
  count = 0
  for letter in string:
    if letter.lower() in plain:
      if count == 5:
        code = code + " "
        count = 0
      code = code + cipher[plain.index(letter.lower())]
      count += 1
  return code

def decode(code):
  plain = "abcdefghijklmnopqrstuvwxyz123456789"
  cipher = "zyxwvutsrqponmlkjihgfedcba123456789"

  string = ""
  for letter in code:
    if letter.lower() in cipher:
      string = string + plain[cipher.index(letter.lower())]
  return string

