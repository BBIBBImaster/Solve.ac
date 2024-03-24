n, m = map(int, input().split())
treeList = list(map(int, input().split()))

def binary_search(target, data):
    start = 0
    end = max(data)
    result = 0

    while start <= end:
        cutSum = 0
        mid = (start + end) // 2

        for tree in data:
            if tree > mid:
                cutSum += tree - mid

        if cutSum < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result

result = binary_search(m, treeList)
print(result)