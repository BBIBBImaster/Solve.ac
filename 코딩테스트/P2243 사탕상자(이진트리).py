import sys

tree = [0]


# 메인함수
n = int(sys.stdin.readline())

for _ in range(n) :
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1 : # 사탕상자에서 사탕을 꺼내는 경우 / b = 꺼낼 사탕의 순위
        print("")
    else :      # 사탕상자 사탕을 넣는 경우 / b = 넣을 맛, c = 넣을 사탕의 개수
        print("")
