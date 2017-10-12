def numeral(number):
  numerals = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
  }

  roman_number = ''

  quotient = 0
  for i in reversed(sorted(numerals.keys())):
    quotient = number/i
    roman_number += numerals[i]*quotient
    number -= quotient*i

  return roman_number

