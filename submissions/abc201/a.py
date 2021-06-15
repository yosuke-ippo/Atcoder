a,b,c = map(int, open(0).read().split())
suuji_list = [a, b, c]
ans_list = sorted(suuji_list)

if ans_list[2] - ans_list[1] == ans_list[1] - ans_list[0]:
  print("Yes")
  
  
else:
  print("No")
