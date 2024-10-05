import sys


if __name__ == "__main__" :
  input = sys.stdin.readline
  k_list = [0]
  s_list = [0]

  k, s = map(int, input().split())
  k_list.append(k)
  s_list.append(s)

  n = int(input())
  
  for _ in range(n) :
    direction, point = map(int, input().split())

    if direction == 1 : 
      k_list.append(point)
      k_list.sort()
    else :
      s_list.append(point)
      s_list.sort()
    
  # 최대 사각형 찾기
  candidate = []
    # 가로 길이
  for i in range(len(k_list)-1) :
    k = k_list[i+1] - k_list[i]
    for j in range(len(s_list) - 1) :
      s = s_list[j+1] - s_list[j]
      candidate.append(k * s)
  
  print(max(candidate))

    

