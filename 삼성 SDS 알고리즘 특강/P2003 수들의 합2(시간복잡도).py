a, b = map(int, input().split())
c = list(map(int, input().split()))

start = 0
end = 0
result = 0
cnt = 0

while True:
    if end == a and result < b:
        break

    if result < b:
        result += c[end]
        end += 1
    elif result >= b:
        if result == b:
            cnt += 1
        result -= c[start]
        start += 1

print(cnt)
