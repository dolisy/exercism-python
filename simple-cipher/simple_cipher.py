import random

class Cipher(object):
  def __init__(self, key = ''):
    self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    self.key = key

    for char in self.key:
      if char not in self.alphabet:
        raise ValueError

    if self.key == '':
      for i in range(1,101):
        self.key += self.alphabet[random.randint(0,25)]

  def encode(self, text):
    code = ''
    for i, letter in enumerate(text):
      if letter.lower() in self.alphabet:
        x = self.alphabet.index(self.key[i % len(self.key)])
        code += self.alphabet[(self.alphabet.index(letter.lower()) + x) % 26]
    return code

  def decode(self, code):
    text = ''
    for i, letter in enumerate(code):
      if letter.lower() in self.alphabet:
        x = self.alphabet.index(self.key[i % len(self.key)])
        text += self.alphabet[(self.alphabet.index(letter.lower()) - x) % 26]
    return text

class Caesar(object):
  def __init__(self):
    self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  def encode(self, text):
    code = ''
    for letter in text:
      if letter.lower() in self.alphabet:
        code += self.alphabet[(self.alphabet.index(letter.lower()) + 3) % 26]
    return code

  def decode(self, code):
    text = ''
    for letter in code:
      if letter.lower() in self.alphabet:
        text += self.alphabet[(self.alphabet.index(letter.lower()) - 3) % 26]
    return text
