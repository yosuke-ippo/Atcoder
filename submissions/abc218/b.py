P = list(map(int,input().split()))
henkan =  lambda c: chr(c+64)
Omoji_list = []

for i in (P):
  Omoji_list += henkan(i)

ans = list(map(str.lower,Omoji_list))  
print("".join(ans))

