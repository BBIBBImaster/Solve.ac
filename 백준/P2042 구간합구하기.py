import sys

n, m, k = map(int, sys.stdin.readline().split())

arr = [0] * (n+1)
tree = [0] * (n+1)

def prefix_sum(i) :
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)       # 효율적인 부모 이동 (비트 AND와 보수 사용)
    return result

def update(i, dif) :
    while i <= n:
        tree[i] += dif
        i += (i & -i)       # 효율적인 자식 이동

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

# 메인루프
for i in range(1, n+1) :
    x = int(input())
    arr[i] = x              # 각 원소를 입력받아 arr 배열에 저장
    update(i, x)            # 각 원소에 대해 update 함수 호출하여 이진 색인 트리를 업데이트

for i in range(m + k) :
    a, b, c = map(int, input().split())
    if a ==1 :
        update(b, c - arr[b])   # 배열의 특정 인덱스 값 업데이트
        arr[b] = c
    else :
        print(interval_sum(b, c))