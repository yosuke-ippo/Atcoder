import math

N = int(input())
kakaku = math.floor(N * 1.08)

if kakaku > 206:
  print(":(")
  
elif kakaku < 206:
  print("Yay!")
  
elif kakaku == 206:
  print("so-so")
  
else:
  pass
