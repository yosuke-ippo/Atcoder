N, A, X, Y = map(int,input().split())

if N > A:
  ans = X * A + (N - A) * Y
  
else:
  ans = X * N
  
print(ans)
