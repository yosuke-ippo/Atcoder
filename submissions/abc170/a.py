A = [int(x) for x in input().split()]
 
ans = 1
for i in A:
  if i == 0:
    print(ans)
  else:
    ans += 1
