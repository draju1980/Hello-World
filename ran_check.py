def ran_check(num,low,high):
  if num >= low and num<= high:
    print(f'{num} is in the range between {low} and {high}')
  else:
    print(f'{num} is not in the range between {low} and {high}')

ran_check(5,2,7)