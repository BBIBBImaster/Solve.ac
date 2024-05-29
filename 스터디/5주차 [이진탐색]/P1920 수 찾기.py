import sys
input = sys.stdin.readline

def binary_search(arr, target) :
    left, right = 0, len(arr) - 1

    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target :
            return True
        elif arr[mid] < target :
            left = mid + 1
        else :
            right = mid - 1
    return False


# 1. 입력 받기
n = int(input())
num_list = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

# 2. 배열 정렬
num_list.sort()

# 3. 각 쿼리에 대해 이진 탐색 수행
results = []
for query in queries :
    if binary_search(num_list, query) :
        results.append(1)
    else :
        results.append(0)

# 4. 결과 출력
for result in results :
    print(result)

