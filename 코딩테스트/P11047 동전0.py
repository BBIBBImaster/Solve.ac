import sys

input = sys.stdin.readline

# 변수 설정
n, k = map(int, input().strip().split())
num_list = []
count = 0

# 숫자 배열 입력받기
for _ in range(n) :
  num = int(input())
  num_list.append(num)

# 숫자 배열 큰 순으로 뒤집기
num_list.sort(reverse=True)

# 최소 동전의 개수 구하기
for coin in num_list :  # 루프를 통해 큰 동전부터 사용
  if k == 0 : 
    break
  if coin <= k :        
    count += k // coin
    k %= coin  # 사용한 동전의 총 가치를 k에서 빼는 코드

print(count)





