#duplicate element identifier
some_list=['a','b','c','c','b','d','e']
dulplicates=[]
for elements in some_list:
  x=some_list.count(elements)
  if x>1 and elements not in dulplicates:
    dulplicates=dulplicates+[elements]
  else:
    pass
print(dulplicates)