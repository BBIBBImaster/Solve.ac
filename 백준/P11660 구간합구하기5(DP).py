import sys

input = sys.stdin.readline

# 표의 크기(n)과 합을 구할 횟수(m) 입력
n, m = map(int, input().split())

# 표 초기화
graph = [ ["0"] * n for i in range(n) ]

# 표 입력받고 그래프에 넣기
for i in range(n) :
    input_list = list(map(int, input().split()))
    for j in range(n) :
        graph[i][j] = input_list[j]

# DP 적용하기 (메모이제이션)
prefix_sum = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0:
            prefix_sum[i][j] = graph[i][j]
        else:
            prefix_sum[i][j] = prefix_sum[i][j - 1] + graph[i][j]

# 원하는 값 구해오기
for _ in range(m):
    result = 0
    # x행 y열
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2):  # 행의 범위 설정
        if y1 == 1:
            result += prefix_sum[i][y2 - 1]
        else:
            result += prefix_sum[i][y2 - 1] - prefix_sum[i][y1 - 2]
    print(result)