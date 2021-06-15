N, K = map(int, input().split())
ans_list= []

for i in range(1,N+1):
  for j in range(1,1+K):
    ans_list.append(str(i)+"0"+str(j))
    
ans_list = [int(x) for x in ans_list]
print(sum(ans_list))
  
