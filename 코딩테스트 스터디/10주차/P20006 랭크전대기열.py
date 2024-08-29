import sys

def ranking_system(p, m, player_list) :
  rooms = []

  for player in player_list :
    level, nickname = int(player[0]), player[1]
    matched = False
    


if __name__ == "__main__" :
  input = sys.stdin.readline
  p, m = map(int, input().split())
  player_list = []

  for _ in range(p) :
    player = list(map(str, input().split()))
    player_list.append(player)

  print(ranking_system(p, m, ranking_system))