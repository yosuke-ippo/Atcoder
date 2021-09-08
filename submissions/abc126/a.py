N, K = map(int, input().split())
S = input()

for i in range(N):
  
  if i == K -1:
    
    if S[i] == 'A':
      ans = (S[0:i]+'a'+S[i+1:])
      
    elif S[i] == 'B':
      ans = (S[0:i]+'b'+S[i+1:])
      
    elif S[i] == 'C':
      ans = (S[0:i]+'c'+S[i+1:])
      
    else:
      pass
  
  else:
    pass
  
print(ans)
