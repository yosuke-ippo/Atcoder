import math

N = int(input())

if N % 2 == 1:
  print((math.floor(N / 2) +1) / N)
  
else:
  print((N / 2) / N)
