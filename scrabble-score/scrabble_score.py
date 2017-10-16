def score(word):
  values = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
  }
  score = 0
  for letter in word:
    for key in values.keys():
      if letter.upper() in key:
        score += values[key]
  return score

print score('m')
