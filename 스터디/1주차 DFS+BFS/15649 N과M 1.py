import sys
input = sys.stdin.readline

def backtracking() :
    # 정답이라면?
    if len(answer) == m :
    # 출력
        print(' '.join(map(str, answer)))
        return
     
    # 정답이 아니라면?
    # 자식노드에 대해
    for i in range(1, n+1) :
    # 정답에 유망
        if i not in answer :
    # 자식으로 이동
            answer.append(i)
    # 재귀
            backtracking()
    # 부모로 이동
            answer.pop()
            
# n = 자연수, m = 수열의 길이
n, m = map(int, input().split())
answer = []

backtracking()


