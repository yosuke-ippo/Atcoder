N, X, T = map(int,input().split())
 
if X >= N:
  print(T)
  
else:
  print(-(-N // X) * T)
