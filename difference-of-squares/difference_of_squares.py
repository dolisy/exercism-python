def square_of_sum(n):
  elements = [x for x in range(1, n + 1)]
  return sum(elements) ** 2

def sum_of_squares(n):
  elements = [x ** 2 for x in range(1, n + 1)]
  return sum(elements)


def difference(n):
  return square_of_sum(n) - sum_of_squares(n)

print difference(10)
