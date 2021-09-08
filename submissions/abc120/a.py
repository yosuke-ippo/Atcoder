A, B, C = map(int,input().split())

if A > B:
  print(0)

else:
  
  if  int(B / A) >= C:
    print(C)
    
  else:
    print(int(B / A))
