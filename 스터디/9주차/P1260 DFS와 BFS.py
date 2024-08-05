# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
import sys
from collections import deque

def create_graph(n, edges) :
  graph = {}
  for i in range(1, n+1) :
    graph[i] = []
  
  for edge in edges :
    v1, v2 = edge
    graph[v1] = graph[v2]
    graph[v2] = graph[v1]

  return graph

def dfs(graph, start) :
  return

def bfs(n, m, v) :
  return

if __name__ == "__main__" :
  input = sys.stdin.readline
  n, m, v = map(int, input().split())
  edges = [list(map(int, input().split())) for _ in range(m)]
