import sys
input = sys.stdin.readline

def backtracking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        answer.append(i)
        backtracking(depth + 1)
        answer.pop()

n, m = map(int, input().split())
answer = []
backtracking(0)
