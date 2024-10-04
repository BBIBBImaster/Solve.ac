import sys

def is_triangle(a, b, c):
    # 삼각형의 성립 여부 확인
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "Invalid"
    
    # 삼각형의 유형 판별
    if sides[0] == sides[1] == sides[2]:
        return "Equilateral"
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return "Isosceles"
    else:
        return "Scalene"

if __name__ == "__main__" :
    input = sys.stdin.readline

    while True : 
        a, b, c = map(int, input().split())
        if a==0 and b==0 and c==0 :
            break
        else :
            print(is_triangle(a, b, c))