import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(str, input().split())))

for _ in range(R):
    for r in range(min(N,M)//2):
        # 초기값 
        x = r
        y = r
        prev_value = graph[y][x]
        # 좌
        for d in range(r+1, N-r):
            y = d
            next_value = graph[y][x]
            graph[y][x] = prev_value
            prev_value = next_value
        # 하
        for d in range(r+1, M-r):
            x = d
            next_value = graph[y][d]
            graph[y][d] = prev_value
            prev_value = next_value
        # 우
        for d in range(r+1, N-r):
            y = N - 1 - d
            next_value = graph[y][x]
            graph[y][x] = prev_value
            prev_value = next_value
        # 상
        for d in range(r+1, M-r):
            x = M - 1 - d
            next_value = graph[y][x]
            graph[y][x] = prev_value
            prev_value = next_value

for n in range(N):
    for m in range(M):
        print(graph[n][m], end=' ')
    print()