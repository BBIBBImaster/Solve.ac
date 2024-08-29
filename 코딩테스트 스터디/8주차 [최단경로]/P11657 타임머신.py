import sys

def bellman_ford(n, edges) :
  distance = [inf] * (n+1)
  distance[1] = 0

  for i in range(n-1) :
    for u,v,w in edges : 
      if distance[u] != inf and distance[u] + w < distance[v] :
        distance[v] = distance[u] + w

  # 음수 사이클 확인
  for u, v, w in edges :
    if distance[u] != inf and distance[u] + w < distance[v] :
      return -1
    
  return distance

if __name__ == "__main__" :
  inf = float('inf')
  input = sys.stdin.readline
  n, m = map(int, input().split())
  edges = []

  for _ in range(m) :
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

  distances = bellman_ford(n, edges)

  if distances == -1 :
    print(-1)
  else :
    for i in range(2, n+1) :
      if distances[i] == inf :
        print(-1)
      else :
        print(distances[i])

