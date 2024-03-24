import sys
sys.setrecursionlimit(1000000)      # 재귀함수의 깊이 설정

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range( n+1 )]  # parent 리스트 생성

def find_parent(x) :
    if parent[x] != x :
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b) :
    a = find_parent(a)
    b = find_parent(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

for _ in range(m) :
    command, a, b = map(int, sys.stdin.readline().split())

    if command == 0 :     # command가 0이면, union 수행
        union_parent(a, b)
    else :          # command가 1이면, find 수행
        if find_parent(a) == find_parent(b) :
            print("YES")
        else :
            print("NO")
