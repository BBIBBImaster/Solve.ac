import sys
input = sys.stdin.readline

def dfs(idx, depth) :
    global min_diff
    # 종료조건 : depth가 n의 절반이 되면(스타트팀과 링크팀이 절반씩)
    if depth == n // 2 :
        start_team = []
        link_team = []
        for i in range(n) :
            if visited[i] :
                start_team.append(i)
            else :
                link_team.append(i)

        start_sum = 0
        link_sum = 0
        for i in range(n//2) :
            for j in range(i+1, n//2) :
                start_sum += ability[start_team[i]][start_team[j]] + ability[start_team[j]][start_team[i]]
                link_sum += ability[link_team[i]][link_team[j]] + ability[link_team[j]][link_team[i]]

        min_diff = min(min_diff, abs(start_sum - link_sum))
        return
    
    # 현재 인덱스부터 시작해서 모든 선수에 대해 방문여부 확인
    for i in range(idx, n) :
        # 방문하지 않은 선수라면, 해당 선수를 start팀에 포함시키고 DFS 재귀 호출
        if not visited[i] :
            visited[i] = True
            dfs(i+1, depth+1)
            # 재귀 호출이 끝나면, 해당 선수를 다시 방문하지 않은 상태로 되돌리기.
            visited[i] = False

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
# 최소값을 갱신할 변수
min_diff = sys.maxsize

dfs(0,0)
print(min_diff)
