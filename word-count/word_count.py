def word_count(sentence):
  import re
  sentence = sentence.lower().replace("_", " ")
  word_count = {}
  for word in re.findall(r"[\w']+", sentence):
    if not word in word_count:
      word_count[word] = 1
    else:
      word_count[word] += 1
  return word_count
