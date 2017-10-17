def primitive_triplets(number_in_triplet):
  if number_in_triplet % 4 == 0:
    return set([(sorted([m**2 - n**2, 2*m*n, m**2 + n**2])[0], sorted([m**2 - n**2, 2*m*n, m**2 + n**2])[1], sorted([m**2 - n**2, 2*m*n, m**2 + n**2])[2]) for m in range(0, number_in_triplet) for n in range(0, number_in_triplet) if 2*m*n == number_in_triplet and m - n > 0 and (m - n) % 2 == 1 and (m % n != 0 or n == 1) and (n % m != 0 or m == 1)])
  else:
    raise ValueError

def triplets_in_range(range_start, range_end):
  return set([(sorted([a,b,c])[0], sorted([a,b,c])[1], sorted([a,b,c])[2]) for a in range(range_start, range_end + 1) for b in range(range_start, range_end + 1) for c in range(range_start, range_end + 1) if a**2 + b**2 == c**2])

def is_triplet(triplet):
  if len([x for x in triplet if x % 4 == 0]) == 1:
    return sorted(list(triplet)) in [sorted(list(x)) for x in primitive_triplets([x for x in triplet if x % 4 == 0][0])]
  else:
    return False

