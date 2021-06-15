K = int(input())
A, B = map(int,input().split())

for i in range(A,B+1):
  if i % K == 0:
    C = 'OK'
    break
    
  elif i == B:
    C = 'NG'
    
  else:
    pass

print(C)
