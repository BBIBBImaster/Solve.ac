def calculate(requests, cut) :
  total_cost = 0
  for req in requests :
    if req > cut :
      total_cost += cut
    else :
      total_cost += req
  return total_cost

def budget(n, requests, m) :
  low, high = 0, max(requests)
  best = 0

  while low <= high :
    mid = (low + high) // 2
    total_cost = calculate(requests, mid)

    if total_cost <= m :
      best = mid
      low += 1
    else :
      high -= 1

  return best

if __name__ == "__main__" :
  import sys
  input = sys.stdin.readline
  n = int(input())
  requests = list(map(int, input().split()))
  m = int(input())

  print(budget(n, requests, m))