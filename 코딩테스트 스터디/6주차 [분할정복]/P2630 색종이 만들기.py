# 색종이 만들기
import sys

input = sys.stdin.readline

n = int(input())
matrix = []

for i in range(n) :
    row = list(map(int, input().split()))
    matrix.append(row)


# 전부 같은 색인가 확인
# 아니면? 쪼개기
def count_paper(matrix, n) :
    white_count = 0
    blue_count = 0

    def divide_and_conquer(x, y, size) :
        nonlocal white_count, blue_count
        current_color = matrix[x][y]
        all_same = True

        for i in range(x, x+size) :
            for j in range(y, y+size) :
                if matrix[i][j] != current_color :
                    all_same = False
                    break
            if not all_same :
                break

        if all_same :
            if current_color == 0 :
                white_count += 1
            else :
                blue_count += 1
        else :
            new_size = size // 2
            divide_and_conquer(x,y,new_size)
            divide_and_conquer(x, y+new_size, new_size)
            divide_and_conquer(x+new_size, y, new_size)
            divide_and_conquer(x+new_size, y+new_size, new_size)

    divide_and_conquer(0,0,n)
    return white_count, blue_count

# 결과 계산
white_count, blue_count = count_paper(matrix, n)

print(white_count)
print(blue_count)