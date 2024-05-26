import copy
import sys
input = sys.stdin.readline

def wall_construction(wall_cnt):
    # 벽이 3개면, 바이러스 퍼트리기
    if wall_cnt == 3:
        virus_spread()
        return
    
    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == 0:  # 벽 세울 수 있는지 확인
                lab_map[i][j] = 1  # 벽 세우기
                wall_construction(wall_cnt + 1)  # 다음 벽 세우기
                lab_map[i][j] = 0  # 백트래킹

def virus_spread():
    global answer
    tmp_map = copy.deepcopy(lab_map)
    virus = [(i, j) for i in range(n) for j in range(m) if tmp_map[i][j] == 2]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 바이러스의 이동 방향 정의

    while virus:
        x, y = virus.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and tmp_map[nx][ny] == 0:
                tmp_map[nx][ny] = 2
                virus.append((nx, ny))  # 바이러스 전파

    safe_cnt = sum(row.count(0) for row in tmp_map)
    answer = max(answer, safe_cnt)


if __name__ == "__main__":
    n, m = map(int, input().split())
    lab_map = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    wall_construction(0)
    print(answer)
