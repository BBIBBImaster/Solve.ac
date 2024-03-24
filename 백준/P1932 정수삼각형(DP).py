import sys

input = sys.stdin.readline

# 삼각형의 크기 입력
n = int(input())

# 삼각형 초기화
graph = []

# 삼각형 입력
for i in range(n) :
    row = list(map(int, input().split()))
    graph.append(row)

# DP테이블 초기화
dp = [[0] * (i+1) for i in range(n)]

# DP테이블 작성 (맨 아래부터 시작/ 그대로)
dp[n-1] = graph[n-1]

for i in range(n-2, -1, -1):
    for j in range(i+1):  # 열의 개수는 해당 층의 인덱스 + 1
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + graph[i][j]

print(dp[0][0])