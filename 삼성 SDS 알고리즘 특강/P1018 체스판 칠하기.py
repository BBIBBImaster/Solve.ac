import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for _ in range(n) :
    row = sys.stdin.readline().rstrip()
    board.append(row)

# n*m 박스를 8*8로 하나씩 순회하기
for i in range(n-7) :
    for j in range(m-7) :
        print("")


# def color_check(board) :
#     start_color = board[0][0]       # 시작 컬러
#
#     # 홀수 행, 홀수 열은 시작 컬러와 색이 같아야 함
#     # 홀수 행, 짝수 열은 시작 컬러와 색이 달라야 함
#     # 짝수 행, 홀수 열은 시작 컬러와 색이 달라야 함
#     # 짝수 행, 짝수 열은 시작 컬러와 색이 같아야 함

