import sys

def DFS (n, m, result, depth) :
    if depth  == m :
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1) :
        if len(result)  == 0 or result[-1] <= i:
            result.append(i)
            DFS(n, m, result, depth+1)
            result.pop()

n, m = map(int, sys.stdin.readline().split())
DFS(n, m, [], 0)


