def encode(plain_text):
  # 1. normalize
  code = plain_text.lower()
  punctuations = [ ' ','.', ',', '!', "'"]
  for punctuation in punctuations:
    code = code.replace(punctuation, '')

  if code == '':
    return ''
  # 2. organize in a rectangle
  l = len(code)
  rest = l**0.5 % 1
  if rest == 0:
    c = int(l**0.5)
    r = int(l**0.5)
  else:
    c = int(l**0.5 - rest + 1)
    r = int(l**0.5 - rest)

  rectangle = []
  for i in range(0, r):
    rectangle.append(code[i*c:i*c + c])

  rectangle[-1] += ' '*(r*c - l)

  # 3. reading down the columns
  columns = []
  for i in range(0, c):
    array = ''
    for j in range(0, r):
      if rectangle[j][i] != ' ':
        array += rectangle[j][i]
    columns.append(array)

  # 4. return in chunks
  return ' '.join(columns)
