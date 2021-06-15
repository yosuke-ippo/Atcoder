N, K = map(int, open(0).read().split())

for i in range(K):
  
  if N % 200 == 0:
    N = int(N / 200)
  else:
    N1 = str(N) + "200"
    N = int(N1)
    
print(int(N))
