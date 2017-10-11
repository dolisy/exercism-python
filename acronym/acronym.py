def abbreviate(words):
  import re
  abreviate = ''
  for word in re.findall(r"[\w']+", words):
    abreviate += word[0].upper()
  return abreviate
