import sys
from collections import deque

# 상하좌우 탐색용 : 현재 (2,2) 일 때, 상(1,2)/ 하(3,2)/ 좌(2,1)/ 우(2,2)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y,  n, m, graph) :
  # 큐 생성 및 초기화
  queue = deque([(x,y)])

  # BFS 시작
  while queue :
    x, y = queue.popleft()

    # 상하좌우 탐색
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]

      # 미로의 범위를 벗어나지 않도록 체크
      if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue

      # 벽(0)이면 무시
      if graph[nx][ny] == 0 :
        continue

      # 처음 방문하는 칸이라면 최단거리 갱신
      if graph[nx][ny] == 1 :
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  return graph[n-1][m-1]

if __name__ == "__main__" :
  input = sys.stdin.readline
  n, m = map(int, input().split())
  graph = [list(map(int, input().strip())) for _ in range(n)]

  print(bfs(0, 0, n, m, graph))
