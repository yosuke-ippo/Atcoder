S = input()
ans1 = S.count(S[0])
ans2 = S.count(S[1])
ans3 = S.count(S[2])
ans4 = S.count(S[3])

if ans1 == 2 and ans2 == 2 and ans3 == 2:
  print('Yes')

else:
  print('No')

