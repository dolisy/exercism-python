def decode(code):
  import re
  string_re = re.compile(r"(\d+|\D)")
  string_list = string_re.findall(code)
  string = []
  for index, x in enumerate(string_list):
    if index == 0:
      if x.isdigit() == False:
        string.append(x)
    else:
      if x.isdigit() == False:
        if string_list[index - 1].isdigit() == True:
          string.append(x * int(string_list[index - 1]))
        else:
          string.append(x)
  return "".join(string)


def encode(string):
  code = []
  count = 0
  for index, letter in enumerate(string):
    if index == 0:
      count += 1
      if string[index] != string[index + 1]:
        code.append(letter)
    elif index == len(string) - 1:
      if string[index] == string[index - 1]:
        count += 1
        code.append(str(count))
        code.append(letter)
      if string[index] != string[index - 1]:
        count = 1
        code.append(letter)
    else:
      if string[index] == string[index - 1]:
        count += 1
        if string[index] != string[index + 1]:
          code.append(str(count))
          code.append(letter)
      if string[index] != string[index - 1]:
         count = 1
         if string[index] != string[index + 1]:
          code.append(letter)
  return "".join(code)
