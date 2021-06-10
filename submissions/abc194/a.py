mushikokei, shibou = map(int, open(0).read().split())
yuushikokei = mushikokei + shibou

if yuushikokei >= 15 and shibou >= 8:
  print(1)
  
else:
  
  if yuushikokei >= 10 and shibou >= 3:
    print(2)
    
  else:
    
    if yuushikokei >= 3:
      print(3)
      
    else:
      print(4)
        

  
