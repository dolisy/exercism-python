def meetup_day(year, month, day, num):
  import datetime
  from datetime import date, datetime, timedelta
  import calendar

  # get last
  last = 0
  day_count = 1
  while month < month + 1:
    try:
      if calendar.day_name[datetime(year, month, day_count).date().weekday()] == day:
        last += 1
      day_count += 1
    except ValueError:
      break

  # get teenth
  teenth = 0
  day_count = 1
  while month < month + 1:
    try:
      if calendar.day_name[datetime(year, month, day_count).date().weekday()] == day:
        teenth += 1
      day_count += 1
    except ValueError:
      break

  # initialize nums
  nums = {
    '1st': 1,
    '2nd': 2,
    '3rd': 3,
    '4th': 4,
    '5th': 5,
    'last': last,
    'teenth': teenth
  }

  # get date
  num_count = 0
  day_count = 1
  while True:
    if calendar.day_name[datetime(year, month, day_count).date().weekday()] == day:
      num_count += 1
      if num_count == nums[num]:
        break
    day_count += 1
  return datetime(year, month, day_count).date()

print meetup_day(2013, 8, 'Wednesday', '4th')






















