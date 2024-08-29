# import sys

# def find_max(n, price_list) :
#   asc_list = sorted(price_list, reverse=False)
#   dsc_list = sorted(price_list, reverse=True)

#   # 쭉 내리막 (이득 0)
#   if price_list == dsc_list :
#     return 0
  
#   # 마지막이 최고가 (1154326) -> 마지막까지 계속 매수
#   elif price_list[-1] == max(price_list) :
#     sum = 0
#     for i in range(n-1) :
#       sum += (price_list[-1] - price_list[i])
#     return sum
  
#   # 오르락 내리락 반복할 경우 -> 최고값이 배열 사이에,,, 
#   # 최고값까지 오르막 계산 / 117436243
#   # 배열 자르고 다시 최대값 계산 / 배열 자르고 다시 최대값 / 배열 자르고 다시 최대값
#   else : 
#     sum = 0
#     i = 0
#     j = 0
#     while price_list[i] == dsc_list[j]:
#       sum += dsc_list[j] - price_list[i] 
#       i += 1
#       if 


#       price_list.popleft()
#     return

# if __name__ == "__main__" :
#   input = sys.stdin.readline

#   t = int(input())
#   for _ in range(t) :
#     n = int(input())
#     price_list = list(map(int, input().split()))
#     print(find_max(n, price_list))
    