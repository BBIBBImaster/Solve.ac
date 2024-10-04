# 행렬곱셈
import sys

input = sys.stdin.readline

matrix_a = []
matrix_b = []

# 행렬 A 입력받기
aN, aM = map(int, input().split())

for i in range(aN) :
    rowA = list(map(int, input().split()))
    matrix_a.append(rowA)

# 행렬 B 입력받기
bN, bM = map(int, input().split())

for j in range(bN) :
    rowB = list(map(int, input().split()))
    matrix_b.append(rowB)


# 행렬 곱셈 함수
def matrix_multiply(a, b) :
    n = len(a)
    m = len(a[0])
    k = len(b[0])
    result = [[0] * k for _ in range(n)]

    for i in range(n) :
        for j in range(k) :
            for l in range(m) :
                result[i][j] += a[i][l] * b[l][j]

    return result

# 결과 수행
result_matrix = matrix_multiply(matrix_a, matrix_b)

# 결과 출력
for row in result_matrix :
    print(" ".join(map(str, row)))

