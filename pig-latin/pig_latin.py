import re

def rule_1(text):
  return text + 'ay'

def rule_2(text, consonant):
  return re.sub(consonant, '', text, count=1) + consonant + 'ay'

def translate_word(text):

  text = text.lower()
  vowels = ['a', 'e', 'i', 'o', 'u']
  exceptions = ['y', 'x', 'squ', 'qu', 'ch', 'thr', 'th', 'ch', 'sch'] # because every rule have their exceptions

  for exception in exceptions:
    if text.startswith(exception):
      if text.replace(exception, '')[0] in vowels:
        return rule_2(text, exception)
      else:
        return rule_1(text)

  for vowel in vowels:
    if text.startswith(vowel):
      return rule_1(text)

  consonant = ''
  for letter in text:
    if letter not in vowels:
      consonant += letter
    else:
      break
  return rule_2(text, consonant)

def translate(sentence):
  text = []
  for word in sentence.lower().split(' '):
    text.append(translate_word(word))

  return ' '.join(text)
