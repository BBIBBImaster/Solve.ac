import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chiken = []
home = []

# 치킨집과 집의 위치를 저장
for i in range(n) : 
    for j in range(n) :
        if graph[i][j] == 1 :
            home.append((i,j))
        elif graph[i][j] == 2 :
            chiken.append((i,j))

answer = 9999
# 치킨집에서 m만큼 조합
chickCombi = list(combinations(chiken, m))

for c in chickCombi :
    long = 0
    for x1, y1 in home :
        street = sys.maxsize
        for x2, y2 in c :
            street = min(street, abs(x1-x2) + abs(y1-y2))
        long += street
    answer = min(answer, long)

print(answer)
