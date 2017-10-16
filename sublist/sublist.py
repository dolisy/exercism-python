SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def check_lists(first_list, second_list):
  if first_list == second_list:
    return EQUAL

  if len(first_list) <= len(second_list):
    lists = {
      'A': first_list,
      'B': second_list,
      True: SUBLIST
    }
  else:
    lists = {
      'B': first_list,
      'A': second_list,
      True: SUPERLIST
    }

  count = 0
  for i in range(0, len(lists['B']) - len(lists['A']) + 1):
    count = 0
    for j in range(0, len(lists['A'])):
      if lists['B'][i + j] == lists['A'][j]:
        count += 1
    if count == len(lists['A']):
      return lists[True]

  return UNEQUAL

