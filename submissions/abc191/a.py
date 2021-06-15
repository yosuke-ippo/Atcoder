V, T, S, D = map(int, open(0).read().split())

byousuu = D / V

if T <= byousuu <= S:
  print("No")
  
else:
  print("Yes")
