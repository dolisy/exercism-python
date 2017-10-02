def detect_anagrams(string, array):
  detect_anagrams = []

  string_dictionary = {}
  for letter in string:
    if letter.lower() in string_dictionary.keys():
      string_dictionary[letter.lower()] += 1
    else:
      string_dictionary[letter.lower()] = 1

  array_redefined = []
  for element in array:
    if element.lower() != string.lower():
      array_redefined.append(element)

  for element in array_redefined:
    element_dictionary = {}
    for letter in element:
      if letter.lower() in element_dictionary.keys():
        element_dictionary[letter.lower()] += 1
      else:
        element_dictionary[letter.lower()] = 1
    if string_dictionary == element_dictionary:
      detect_anagrams.append(element)

  return detect_anagrams
