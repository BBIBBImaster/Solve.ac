import sys
inf = int(1e9)      # 무한대 값 설정

input = sys.stdin.readline

# 도시의 개수(n), 버스의 개수(m) 입력
n = int(input())
m = int(input())

# 그래프 초기화
graph = [ [inf] * n for _ in range(n) ]

# 버스 노선 정보 입력
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

# 플로이드-워셜 알고리즘 수행
# 현재까지의 최단경로와 새로운 경로를 비교하여 갱신
# 1. k는 경유하는 노드를 의미, 즉 모든 노드를 순회
# 2. i는 출발노드를, j는 도착노드를 의미
# 3. graph[i][j]는 i에서 j로 가는 비용을 의미
# 4. graph[i][k] + graph[k][j]는 i에서 j로 가는데 k를 경유하여 가는 경로의 비용
for k in range (n) :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 자기 자신으로 가능 비용 0으로 초기화
for i in range(n) :
    for j in range(n) :
        if i == j :
            graph[i][j] = 0

# 출력
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == inf :
            print(0, end=' ')
        else :
            print(graph[i][j], end=' ')
    print()