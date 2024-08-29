import sys

input = sys.stdin.readline

# 수의 개수(n)과 합을 구해야 하는 횟수(m) 입력
n, m = map(int, input().split())

# n개의 수 입력
num_list = list(map(int, input().split()))

# get_sum 함수
def get_sum(n) :
    prefix_sum = [0] * (n+1)        # 누적 합을 저장하기 위한 배열을 초기화
    for i in range(1, n+1) :
        prefix_sum[i] = prefix_sum[i-1] + num_list[i-1]
    return prefix_sum

# 합을 구해야 하는 구간 i, j 입력
prefix_sum = get_sum(n)
for _ in range(m) :
    i, j = map(int, input().split())
    result = prefix_sum[j] - prefix_sum[i-1]
    print(result)
