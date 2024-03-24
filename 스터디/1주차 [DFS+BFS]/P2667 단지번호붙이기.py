import sys
input = sys.stdin.readline

# 정n각형
n = int(input())
# 그래프 생성
map = [list(map(int,input().strip())) for _ in range(n)]

# 위, 아래, 오른쪽, 왼쪽으로 이동
d = [(1,0), (0,1), (-1,0), (0,-1)]
count = 0

def dfs(y,x) :
    # 지도를 벗어나면 멈춘다
    if (x < 0) or (x >= n) or (y < 0) or (y >= n) :
        return False
    # 집이면 수행
    if map[y][x] == 1 :
        global count
        count += 1
        # 확인한 집은 0으로
        map[y][x] = 0
        # 같은 단지 이웃 찾기
        for dx, dy in d :
            dfs(y + dy, x + dx)
        return True
    return False

# 이웃 수
sum = []
for i in range(n) :
    for j in range(n) :
        if dfs(i, j) :
            sum.append(count)
            # 다른 단지 찾기 위해 초기화
            count = 0

# 이웃 수 -> 오름차순
sum.sort()
# 단지의 개수, 단지 내의 집 수 출력
print(len(sum))
for i in range(len(sum)) :
    print(sum[i])
