N = int(input())
N_list = list(range(1,N+1))
A = sorted([int(i) for i in input().split()])

if N_list == A:
  print('Yes')
  
else:
  print('No')
