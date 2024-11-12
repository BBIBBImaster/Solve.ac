import sys
sys.setrecursionlimit(10000)

def dfs(v, graph, visited) :
  visited[v] = True
  for neighbor in graph[v] :
    if not visited[neighbor] :
      dfs(neighbor, graph, visited)

if __name__ == "__main__" :
  input = sys.stdin.readline
  n, m = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  visited = [False] * (n+1)

  # 간선 입력
  for _ in range(m) :
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

  component_count = 0

  for i in range(1, n+1) :
    if not visited[i] :
      dfs(i, graph, visited)
      component_count += 1

  print(component_count)