import sys

input = sys.stdin.readline

# 1. 입력받기
k, n  = map(int, input().split())
num_list = []
for _ in range(k) :
    x = int(input())
    num_list.append(x)

# 2. 배열 정렬
num_list.sort()

# 3. 이진 함수 탐색
def binary_search(arr, n) :
    result = 0
    left, right = 1, max(arr)

    while left <= right :
        mid = (left + right) // 2
        count = sum(x // mid for x in arr)

        if count >= n : # 원하는 개수 이상을 만들었으면,
            result = mid # 가능한 길이 중, 가장 긴 길이
            left = mid + 1  # 더 긴 길이 시도
        else : # 원하는 개수 미만이면,
            right = mid - 1 # 더 짧은 길이 시도
    
    return result

# 4. 결과 출력
print(binary_search(num_list,n))

    


