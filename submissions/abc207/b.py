A, B, C, D = map(int, input().split())
diff = C*D-B
count = 0
 
if diff <= 0:
  count = -1
  print(count)
    
else:
  count = (A+diff-1)//diff
  print(count)
