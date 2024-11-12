import sys

def ranking (n, k, medal_list) :
  medal_list.sort(key=lambda x : (x[1], x[2], x[3]), reverse = True)

  ranking_list = []
  for i in range(n) :
    ranking_list.append(medal_list[i][0])

  return ranking_list.index(k)

if __name__ == "__main__" :
  input = sys.stdin.readline
  n, k = map(int, input().split())
  medal_list = []

  for _ in range(n) :
    c, g, s, b = map(int, input().split())
    medal_list.append([c,g,s,b])

  print(ranking(n, k, medal_list))