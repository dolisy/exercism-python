def largest_product(series, size):
  if size > len(series) or size < 0:
    raise ValueError
  elif series == '':
    return 1
  else:
    largest_product = []
    product = 1
    for i in range(0, len(series) - size + 1):
      product = 1
      for j in range(0, size):
        product = product * int(series[i + j])
      largest_product.append(product)

    return max(largest_product)
