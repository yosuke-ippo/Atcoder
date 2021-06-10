S = list(input())
R = [""] * len(S)
yousosuu = len(S) +1

for i in range(len(S)):
  j = i + 1
  if S[i] == "0":
    R[-j] = "0"
  elif S[i] == "1":
    R[-j] = "1"
  elif S[i] == "8":
    R[-j] = "8"
  elif S[i] == "9":
    R[-j] = "6"
  elif S[i] == "6":
    R[-j] = "9"
  else:
    pass

print("".join(R))
