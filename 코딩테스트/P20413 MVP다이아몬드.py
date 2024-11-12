import sys

def maximum_pay(n, s, g, p, d, rank_history) :
  total_payment = 0

  # 초기화
  limit = {'B':s-1, 'S':s, 'G':g, 'P':p, 'D':d}
  ranks = ['B','S','G','P','D']
  last_pay = limit[rank_history[0]]
  total_payment += last_pay
  
  # 순차 시행
  for i in range(1, n) :
    current_rank = rank_history[i]
    if current_rank == 'D' :
      total_payment += limit['D']

    next_rank_index = ranks.index(current_rank) + 1
    
    # next_rank_index가 ranks의 범위를 벗어나지 않도록 처리
    if next_rank_index < len(ranks):
        pay_i = limit[ranks[next_rank_index]] - last_pay - 1
        last_pay = pay_i
        total_payment += last_pay



  return total_payment



if __name__ == "__main__" :
  input = sys.stdin.readline
  n = int(input()) 
  s, g, p, d = map(int, input().split())
  rank_history = list(input())

  print(maximum_pay(n, s, g, p, d, rank_history))

