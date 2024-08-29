
import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

# a를 b번 곱한 수를 c로 나눈 나머지를 구하는 프로그램
def modular_exponentiation(a, b, c) :
    if b == 0 :
        return 1
    if b == 1 :
        return a % c
    
    # Divide and Conquer
    half = modular_exponentiation(a, b // 2, c)
    half = (half * half) % c

    if b % 2 == 0 :
        return half
    else : 
        return (half * a) % c
    

# 결과 계산 및 출력
result = modular_exponentiation(a, b, c)
print(result)
