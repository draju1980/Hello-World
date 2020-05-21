def unique_list(lst):
  newlist=[]
  for x in lst:
    if x  not in newlist:
      newlist.append(x) 

  return newlist


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))