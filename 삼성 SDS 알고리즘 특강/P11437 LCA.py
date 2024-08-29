# 1. 인접리스트를 입력받는다
# 2. parent(부모 노드 기록), depth(노드의 깊이 기록), visited(방문 여부 기록) 정의
# 3. 루트 노드인 1부터, 각 노드의 depth 기록해준다(make_depth)
#    - 방문 여부를 확인하면 해당 노드와 연결된 노드에 깊이(dep)를 1씩 증가 시키면서 기록
# 4. 테스트케이스만 공통조상 탐색
#    (1) x노드와 y노드 중 가장 깊이가 깊은 노드를 y로 통일
#    (2) 깊이가 같아질 때까지 y를 parent[y]로 업데이트
#    (3) 두 노드의 깊이만큼 부모를 거슬러 올라간다. x==y 이면 브레이크하고 return x
# 5. return 값을 print

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def make_depth(node, dep) :
    visited[node] = True
    depth[node] = dep
    for nnode in arr[node] :
        if not visited[nnode]:
            parent[nnode] = node
            make_depth(nnode, dep+1)

def lca(x, y) :
    if depth[x] > depth[y] :
        y, x = x, y
    while True :
        if depth[x] == depth[y]:
            break
        y = parent[y]
    for _ in range[depth[x]] :
        if x == y :
            return x
        x = parent[x]
        y = parent[y]
    return x

N = int(input())
arr = [ [] for _ in range(N+1) ]
for _ in range(N-1) :
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

parent = [i for i in range(N+1)]
depth = [0] * (N+1)
visited = [False] * (N+1)
make_depth(1, 0)

T = int(input())
for _ in range(T) :
    x, y = map(int, input().split())
    print(lca(x, y))