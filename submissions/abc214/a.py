N = int(input())

if N < 126:
  ans = 4
  
elif 125 < N and N < 212:
  ans = 6
  
else:
  ans = 8
  
print(ans)
  
  
