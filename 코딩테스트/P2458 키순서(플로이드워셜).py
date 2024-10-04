import sys
inf = 1
input = sys.stdin.readline

# 학생의 수(n)과 비교한 횟수(m) 입력
n, m = map(int, input().split())

# 그래프 초기화
graph = [ [inf] * n for _ in range(n) ]

# 학생 키 정보 입력 & 그래프 갱신
for _ in range(m) :
    a, b = map(int, input().split())
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = 0
            
# 자기 자신과의 비교(0) 초기화
for i in range(n) :
    for j in range(n) :
        graph[i][j] = 0

# 출력 (몇명인지 확인)