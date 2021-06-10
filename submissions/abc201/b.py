N = int(input())

yama_list =[]

for i in range(N):
  namae, takasa = input().split()
  takasa = int(takasa)
  yama_list.append([namae,takasa])
  
ans_list = sorted(yama_list, reverse= True, key=lambda x: x[1])

print(ans_list[1][0])

  
