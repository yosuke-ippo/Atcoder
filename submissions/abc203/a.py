a, b, c = map(int, open(0).read().split())
ans_list =[a, b, c]
x = len(set(ans_list))

if x == 3:
  print(0)

elif x == 1:
  print(a)
  
else:
  if ans_list.count(a) == 1:
    print(a)
    
  elif ans_list.count(b) == 1:
    print(b)
    
  elif ans_list.count(c) == 1:
    print(c)
    
  else:
    pass
    
