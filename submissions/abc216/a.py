X, Y = map(int, input().split('.'))

if Y < 3:
  print(str(X)+'-')
  
elif Y < 7:
  print(str(X))
  
else:
  print(str(X)+'+')
