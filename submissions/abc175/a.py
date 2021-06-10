S = input()
count = 0

for i in range(3):
  if S[i] == 'R':
    
    if count == 0:
      count += 1
      
    elif S[i] == S[i-1]:
      count += 1
      
    else:
      pass
    
  else:
    pass
  
print(count)
