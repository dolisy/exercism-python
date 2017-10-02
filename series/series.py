def slices(string, series):
  if series <= len(string) and series > 0:
    slices = []
    for string_index in range(0,len(string) - series + 1):
      slice = []
      for slice_index in range(0, series):
        slice.append(int(string[string_index + slice_index]))
      slices.append(slice)
    return slices
  else:
    raise ValueError('The sequences are not equal in length')
