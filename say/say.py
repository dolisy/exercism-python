spell = {
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety'
}

higher_ranks = {
  1000: ' thousand ',
  1000000: ' million ',
  1000000000: ' billion '
}

def rank_2_spell(number):
  if number < 20:
    return spell[number]
  elif number < 100:
    if number - int(str(number)[0])*10 == 0:
      return spell[int(str(number)[0])*10]
    else:
      return "%s-%s" % (spell[int(str(number)[0])*10], spell[number - int(str(number)[0])*10])

def rank_3_spell(number):
  if number < 100:
    return rank_2_spell(number)
  elif number < 1000:
    if rank_2_spell(number - 100*int(str(number)[0])) == 'zero':
      return "%s hundred" % (spell[int(str(number)[0])])
    else:
      return "%s hundred and %s" % (spell[int(str(number)[0])], rank_2_spell(number - 100*int(str(number)[0])))

def say(number):
  if number < 0 or number > 999999999999:
    raise AttributeError
  elif number == 0:
    return 'zero'
  else:
    say = ''
    sequence = [1000000000, 1000000, 1000, 1]
    rank = 0
    x = number

    for n in sequence:
      rank = x / n
      if say != '' and x < 100 and rank != 0:
        say += 'and '
      if rank != 0:
        say += rank_3_spell(rank)
        if n >= 1000:
          say += higher_ranks[n]
      x = x - rank * n

    return say.rstrip()















