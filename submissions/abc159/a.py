import itertools

N, M = map(int,input().split())

NM_list = list(range(0,N+M))
ans_list = list(itertools.combinations(NM_list, 2))
print(len(ans_list) - N * M)
