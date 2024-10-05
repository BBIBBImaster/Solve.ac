import sys

# 상하좌우 이동용 (2,2)일 때, 상(1,2) 하(3,2) 좌(2,1) 우(2,3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
  global count
  visited[x][y] = True # 방문했다는 의미
  count += 1

  # 상하좌우 탐색
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
      dfs(nx, ny)

if __name__ == "__main__" :
  input = sys.stdin.readline
  n = int(input())
  graph = [list(map(int, input().strip())) for _ in range(n)]
  visited = [[False] * n for _ in range(n)]
  complexes = []

  for i in range(n) :
    for j in range(n) :
      if graph[i][j] == 1 and not visited[i][j] :
        count = 0
        dfs(i, j)
        complexes.append(count)
  
  print(len(complexes))
  complexes.sort()
  for i in range(len(complexes)) :
    print(complexes[i])