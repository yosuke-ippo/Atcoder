C = input()
moji_list = [chr(i) for i in range(97, 97+26)]

index_C = moji_list.index(C)
print(moji_list[index_C +1])
