# 2���T���̊֐�
def binary_search(B,K):

#�E�[�ƍ��[�̃C���f�b�N�X
  left_index = 0
  right_index = len(B) - 1

#���Ԃ̃C���f�b�N�X�łQ�����Ēl��T��
  while right_index - left_index > 1:
    middle_index = (left_index + right_index) // 2
    middle_value = B[middle_index]

#�ő�l��K�ȏ�̏ꍇ�͂Q�������C���f�b�N�X���E�[�ɂ���        
    if middle_value >= K:
      right_index = middle_index

#�ő�l��K���傫���ꍇ�͂Q�������C���f�b�N�X���E�[�ɂ���        
    else:
      left_index = middle_index
  
  return right_index

          
#�W������
N, Q =map(int, input().split())

#����A�������\�[�g
A = sorted([int(x) for x in input().split()])

#A[i]�̎��_��A[i]�ȉ��A������A�Ɋ܂܂�Ȃ������̐������X�g��(=���X�gS)
#�v�f��A�̗������Ă���A���H���č쐬
S = [0 for i in range(len(A))]

#�ŏ��̐�����A[0]-1
S[0] = A[0] -1

#������̐���=[S�̑O�̐���+A[i]��A[-1]�ɂȂ���]
#A[i]��A[-1]�̍���1���ƘA�����������ɂȂ��Ă��܂�����-1������
for i in range(1,len(A)):
  S[i] = S[i-1] + (A[i] - A[i-1]-1)

#K�̏���  
for j in range(Q):
  K = int(input())
  
#�@K��A�̍ő�l���傫���ꍇ�̉�=[A�̍ő�l+(K-S�̍ő�l)]    
  if K > S[-1]:
    ans = A[-1] + (K - S[-1])
    print(ans)

#�AK��A�̍ŏ��l�����̏ꍇ�̉�=[K]
#S[0]��(A[0]-1)�Ȃ̂�>=�Ŕ���
  elif S[0] >= K:
    ans = K
    print(ans)

#�BA�̊Ԃ�K������ꍇ�̉�=[�Q���T���������ʂ̒l]
  else:
    X = binary_search(S, K)
    ans = (A[X] - 1) - (S[X] - K)
    print(ans)
