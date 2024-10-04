import sys
from collections import deque

input = sys.stdin.readline

def rotate(idx, dir) :
    print("")



if __name__ == "__main__":
    gears = [deque(map(int, input().rstrip())) for _ in range(4)]
    k = int(input())
    info = [tuple(map(int, input().split())) for _ in range(k)]
    print(gears, k, info)
    