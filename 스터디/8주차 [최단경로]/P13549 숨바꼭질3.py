import sys
import heapq

def find_friend_dijkstra(n, k):
  limit = 100000
  inf = float('inf')
  # 최단 시간 배열 초기화
  distance = [inf] * (limit + 1)  
  distance[n] = 0

  # 우선순위 큐 초기화
  priority_queue = [(0,n)] # 현재 시간 / 현재 위치

  while priority_queue :
    current_time, current_pos = heapq.heappop(priority_queue)

    # 현재 위치가 친구 위치랑 같으면,
    if current_pos == k :
      return current_time
    
    # 현재 위치에서 가능한 이동
    next_position = [
      (current_time+1, current_pos-1), # 뒤로 1칸 걷기 (시간 +1)
      (current_time+1, current_pos+1), # 앞으로 1칸 걷기 (시간 +1)
      (current_time, current_pos * 2)  # 순간이동 *2 (시간 그대로)
    ]

    for next_time, next_pos in next_position:
      if 0 <= next_pos <= limit and next_time < distance[next_pos] :
        distance[next_pos] = next_time
        heapq.heappush(priority_queue, (next_time, next_pos))

  return 

if __name__ == "__main__" :
  input = sys.stdin.readline
  n, k = map(int,input().split()) # n: 수빈 위치/ k: 친구 위치
  print(find_friend_dijkstra(n, k))