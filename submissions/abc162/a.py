N = input()
ans =""

for i in range(len(N)):
  if N[i] =="7":
    ans = "Yes"
    break
  
  elif i == 2 and N[i] !="7":
    ans = "No"
  
  else:
    pass
  
print(ans)
