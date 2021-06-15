A, B= map(int, input().split())

goukei_a = sum(list(map(int, str(A))))
goukei_b = sum(list(map(int, str(B))))

if goukei_a >= goukei_b:
  print(goukei_a)
  
else:
  print(goukei_b)

