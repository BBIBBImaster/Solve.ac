import sys

input = sys.stdin.readline

n = int(input())
matrix = []

for i in range(n) : 
    row = list(map(int, input().strip()))
    matrix.append(row)

def quad_tree(x, y, size) :
    if size == 1 :
        return str(matrix[x][y])
    
    half_size = size // 2
    parts = [
        quad_tree(x, y, half_size),
        quad_tree(x, y+half_size, half_size),
        quad_tree(x+half_size, y, half_size),
        quad_tree(x+half_size, y+half_size, half_size)
    ]

    # 압축 가능한 경우 (모두 같을 경우)
    if parts[0] == parts[1] == parts[2] == parts[3] and len(parts[0]) == 1: 
        return parts[0]
    # 압축 하지 못 할 경우
    else :
        return "(" + "".join(parts) + ")"
    
# 결과 계산 및 출력
result = quad_tree(0, 0, n)
print(result)