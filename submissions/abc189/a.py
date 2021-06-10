slot = input()

for i in range(len(slot)):
    
  if len(slot)-1 == i:
    print("Won")
    break
  
  elif slot[i] == slot[i+1]:
    continue
    
  else:
    print("Lost")
    break
