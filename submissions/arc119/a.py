N = int(input())
i = 0
x = 0
a = 0 
b = 0
c = 0
suuji_list =[]

while True:
  x = 2 ** i
  i = i + 1
  
  if i > 1: 
    b = i - 1
    y = 2 ** b
    a = N // y
    c = N %  y
    suuji_list.append(a +b +c)
    if x > N:
      break
  
  elif 2 > N:
    print(1)
    exit()
    
  else:
    pass
  
print(min(suuji_list))
