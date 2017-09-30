def hey(string):
  if string.split() == []:
    return 'Fine. Be that way!'
  elif string.upper() == string and string.lower() != string:
    return 'Whoa, chill out!'
  elif "?" in string.split()[-1]:
    return 'Sure.'
  else:
    return 'Whatever.'
