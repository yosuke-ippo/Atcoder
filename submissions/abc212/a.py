A, B = map(int, input().split())

if A > 0 and B == 0:
  print('Gold')
  
elif A == 0 and B > 0:
  print('Silver')
  
elif A > 0 and B > 0:
  print('Alloy')
  
else:
  pass
  