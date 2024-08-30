import sys
from collections import deque   

def josephus_problem(n, k):
    queue = deque(range(1, n + 1))
    result = []

    while queue:
        queue.rotate(-(k - 1))  # k-1번 왼쪽으로 회전
        result.append(queue.popleft())  # k번째 사람 제거
    
    return result

if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())
    result = josephus_problem(n, k)

    print("<" + ", ".join(map(str, result)) + ">")