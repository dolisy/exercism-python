def flatten(iterable):
  string = str(iterable)
  string = string.replace('[', '')
  string = string.replace(']', '')
  string = string.replace(',', '')
  string = string.replace('(', '')
  string = string.replace(')', '')

  array = string.split(" ")

  result = []

  for element in array:
    try:
      result.append(float(element))
    except ValueError:
      string_element = element.replace("'", "")

      if string_element != 'None' and string_element != '':
        result.append(str(string_element))

  return result
