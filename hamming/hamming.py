def distance(sequence_a, sequence_b):
  distance = 0
  if len(sequence_a) == len(sequence_b):
    for a, b in zip(sequence_a, sequence_b):
      if a != b:
        distance += 1
    return distance
  else:
    raise ValueError('The sequences are not equal in length')




