# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
  newtxt=''
  for item in text:
    newtxt=newtxt+item*3
  print(newtxt)


paper_doll('Hello')