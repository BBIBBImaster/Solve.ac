# 인디그리
# 간선 삭제 (10만개 -> 간선 배열? 간선 리스트 선언)

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []                                    # 간선 정보를 담을 배열
inDegree = [ 0 for i in range(32001)]       # 각 노드의 진입차수 배열 초기화
graph = [[] for i in range(32001)]          # 인접리스트를 나타내기 위한 배열
queue = deque()                             # 위상정렬을 위한 큐 생성

for i in range(m):                          # 간선 정보를 입력받음
    a, b = map(int, input().split())
    arr.append([a, b])

for a, b in arr:
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    #indegree가 0인 정점을 제거하고, 해당 정점이 참조하고있던 점들의 indegree를 감소시킨다.
    for j in graph[student]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            queue.append(j)
    print(student, end = ' ')