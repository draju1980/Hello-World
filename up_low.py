def up_low(s):
  s_upp=[]    # isupper()
  s_low=[]    # islower()
  for char in s:
    if char.isupper() == True:
      s_upp.append(char)
    elif char.islower() == True:
      s_low.append(char)
    else:
      pass

  print(f'No. of Upper case characters :  {len(s_upp)}')
  print(f'No. of Lower case Characters :  {len(s_low)}')
 



s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))
