N, X = map(int,input().split())
A = list(map(int, input().split()))
B = 0

for i in range(N):
  
  if  i % 2 == 0:
    B += A[i]
  
  else:
    B += (A[i] -1)
    
if B > X:
  print('No')
  
else:
  print('Yes')

  

