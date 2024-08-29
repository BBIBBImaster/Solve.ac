import sys

input = sys.stdin.readline

n = int(input())
matrix = []

for i in range(n) :
    row = list([map(int, input().split())])
    matrix.append(row)

# 9개로 쪼개기
def count_paper(matrix, x, y , size, counts) :
    initial = matrix[x][y]
    all_same = True

    for i in range(x, x+size) :
        for j in range(y, y+size) :
            if matrix[i][j] != initial :
                all_same = False
                break
        if not all_same :
            break

    if all_same :
        count[initial + 1] += 1

    else :
        new_size = size // 3
        for dx in range(3) :
            for dy in range(3) :
                count_paper(matrix, x + dx)