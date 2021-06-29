ST = input().split()
AB = input().split()
U = input()

if ST[0] == U:
  print(int(AB[0])-1,int(AB[1]))
  
else:
  print(int(AB[0]),int(AB[1])-1)
