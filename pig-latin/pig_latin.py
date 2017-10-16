import re

def rule_1(text):
  return text + 'ay'

def rule_2(text, consonant):
  return re.sub(consonant, '', text, count=1) + consonant + 'ay'

def translate(text):
  vowels = ['a', 'e', 'i', 'o', 'u']

  for i in range(0, len(text)):
    if


print translate("xray") #, "xrayay"


