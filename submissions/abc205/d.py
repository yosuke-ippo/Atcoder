# 2分探索の関数
def binary_search(B,K):

#右端と左端のインデックス
  left_index = 0
  right_index = len(B) - 1

#中間のインデックスで２分して値を探す
  while right_index - left_index > 1:
    middle_index = (left_index + right_index) // 2
    middle_value = B[middle_index]

#最大値がK以上の場合は２分したインデックスを右端にする        
    if middle_value >= K:
      right_index = middle_index

#最大値がKより大きい場合は２分したインデックスを右端にする        
    else:
      left_index = middle_index
  
  return right_index

          
#標準入力
N, Q =map(int, input().split())

#数列Aを昇順ソート
A = sorted([int(x) for x in input().split()])

#A[i]の時点でA[i]以下、且つ数列Aに含まれない数字の数をリストへ(=リストS)
#要素数Aの列を作ってから、加工して作成
S = [0 for i in range(len(A))]

#最初の数字はA[0]-1
S[0] = A[0] -1

#次からの数字=[Sの前の数字+A[i]とA[-1]にない数]
#A[i]とA[-1]の差が1だと連続した数字になってしまうため-1をする
for i in range(1,len(A)):
  S[i] = S[i-1] + (A[i] - A[i-1]-1)

#Kの処理  
for j in range(Q):
  K = int(input())
  
#①KがAの最大値より大きい場合の解答=[Aの最大値+(K-Sの最大値)]    
  if K > S[-1]:
    ans = A[-1] + (K - S[-1])
    print(ans)

#②KがAの最小値未満の場合の解答=[K]
#S[0]は(A[0]-1)なので>=で判定
  elif S[0] >= K:
    ans = K
    print(ans)

#③Aの間にKがある場合の解答=[２分探索した結果の値]
  else:
    X = binary_search(S, K)
    ans = (A[X] - 1) - (S[X] - K)
    print(ans)
