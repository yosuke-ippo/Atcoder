ninzuu = int(input())
A = [0] * ninzuu
B = [0] * ninzuu

for i in range(ninzuu):
    A[i], B[i] = map(int, input().split())
    
A_saisyoindex = A.index(min(A))
B_saisyoindex = B.index(min(B))

if A_saisyoindex !=  B_saisyoindex:
  print(max(min(A), min(B)))
   
else:
  A_sortlist =sorted(A)
  B_sortlist =sorted(B)
  saisyo1 = min(A)+ min(B)
  saisyo2 = max(min(A), B_sortlist[1])
  saisyo3 = max(A_sortlist[1], min(B))
  print(min(saisyo1, saisyo2, saisyo3))
