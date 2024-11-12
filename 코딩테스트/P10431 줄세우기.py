import sys
from collections import deque

def find_count(tc_list) :
  count = 0
  tc_list = tc_list[1:]

  target_list = deque()
  target_list.append(tc_list[0])

  for i in range(1, 20):
    # 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
    if target_list[-1] < tc_list[i] :
      target_list.append(tc_list[i])
    # 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다.
    # 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.
    else :
      for j in range(len(target_list)) :
        if target_list[j] > tc_list[i] :
          target_list.insert(j, tc_list[i])
          count += len(target_list) - (j + 1)
          break

  return count

if __name__ == "__main__" :
  input = sys.stdin.readline
  p = int(input())
  tc_list = []

  for _ in range(p) :
    tc = list(map(int, input().split()))
    print(tc[0],find_count(tc))


