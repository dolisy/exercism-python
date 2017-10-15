def transform(legacy_data):
  data = {}
  for key, value in legacy_data.items():
    for letter in value:
      data[letter.lower()] = key
  return data









legacy_data = {1: ["A", "E", "I", "O", "U"]}
print transform(legacy_data) # data = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
