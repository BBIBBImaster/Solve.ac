import sys

input = sys.stdin.readline

# 1. 입력받기
n, c = map(int, input().split())
wifi_list = []
for _ in range(n) :
    x = int(input())
    wifi_list.append(x)

# 2. 배열 정렬
wifi_list.sort()

# 3. 이진 탐색 함수 구현
def binary_search (arr, t)
