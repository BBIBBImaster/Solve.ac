import sys

input = sys.stdin.readline

n, m = map(int, input().split())
treeList = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점
start = 1
end = max(treeList)

# 이진 탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in treeList:
        # 잘랐을 때의 나무 길이 계산
        if tree > mid:
            total += tree - mid
    # 나무 길이가 부족한 경우 더 많이 자르기
    if total < m:
        end = mid - 1
    # 나무 길이가 충분한 경우 덜 자르기
    else:
        start = mid + 1

print(end)
