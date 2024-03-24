import sys

def dfs(count, index) :
    if count -1 == m :
        print(' '. join(map(str, list)))
        return
    
    for i in range(index, n+1) :
        list.append(i)
        dfs(count+1, i)
        list.pop()

n, m = map(int, sys.stdin.readline().split())
list = []

dfs(1,1)