import sys
import heapq

def disjkstra(start, n, graph) :
  inf = float('inf')
  distance  = [inf] * (n+1) # 모든 정점의 최단 거리를 무한대로 초기화
  distance[start] = 0 # 시작 정점의 거리는 0
  priority_queue = [(0, start)] # (거리, 정점)의 형태로 우선순위 큐 초기화

  while priority_queue : # 우선순위 큐가 빌 때까지 반복
    current_distance, current_node = heapq.heappop(priority_queue) # 가장 작은 거리를 가진 정점 꺼내기

    if current_distance > distance[current_node] :
      continue

    for neighbor, weight in graph[current_node] : # 인접 정점 확인
      distance_through_current = current_distance + weight # 현재 정점을 거쳐서 가는 새로운 거리 계산
      if distance_through_current < distance[neighbor] : # 새로운 거리가, 기존 거리보다 작다면 업데이트
        distance[neighbor] = distance_through_current
        heapq.heappush(priority_queue, (distance_through_current, neighbor))

  return distance

def find_shortest(n, graph, v1, v2) :
  dist_from_1 = disjkstra(1, n, graph)
  dist_from_v1 = disjkstra(v1, n, graph)
  dist_from_v2 = disjkstra(v2, n, graph)
  
  path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
  path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

  return min(path1, path2)


if __name__ == "__main__" :
  input = sys.stdin.readline
  n, e = map(int, input().split())
  graph = [[] for _ in range(n+1)]

  for _ in range(e) :
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

  v1, v2 = map(int, input().split())

  print(find_shortest(n, graph, v1, v2))


