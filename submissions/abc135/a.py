A, B = map(int,input().split())
 
K = int((A + B) / 2)
if abs(A - K) == abs(B - K):
  print(K)
  
else:
  print('IMPOSSIBLE')
