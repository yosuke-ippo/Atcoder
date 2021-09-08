tenki = ['Sunny', 'Cloudy', 'Rainy']
S = input()

ans_index = tenki.index(S)

if ans_index == 2:
  print(tenki[0])

else:
  print(tenki[ans_index+1])
