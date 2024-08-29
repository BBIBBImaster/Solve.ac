def min_cost(n, distances, prices) :
  total_cost = 0
  min_price = prices[0]

  for i in range(n-1) :
    if prices[i] < min_price :
      min_price = prices[i]

    total_cost += min_price * distances[i]

  return total_cost

if __name__ == "__main__" :
  import sys
  input = sys.stdin.readline
  n = int(input())
  distances = list(map(int, input().split()))
  prices = list(map(int, input().split()))

  print(min_cost(n, distances, prices))
