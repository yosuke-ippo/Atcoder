N = int(input())
ans = 0

ans_list =list(map(int,input().split()))

for i in ans_list:
  
  if i > 10:
    ans += (i -10)
  
  else:
    pass
  
print(ans)
