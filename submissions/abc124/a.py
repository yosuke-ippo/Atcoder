A, B =map(int,input().split())
ans_list =[A, A-1, B, B-1]
ans_list.sort(reverse=True)

print(ans_list[0]+ans_list[1])
