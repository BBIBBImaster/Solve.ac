import sys
import itertools

def find_max(c, player_list) :
  for i in range(c) :
    # 해당 테스트 케이스의 선수 리스트
    max_sum = 0
    abilities = player_list[i] # i번째 테스트 케이스의 선수 능력치들
    players = list(range(11)) 

    for perm in itertools.permutations(players) :
      current_sum = 0
      for pos in range(11) :
        current_sum += abilities[perm[pos]][pos]
      max_sum = max(max_sum, current_sum)

    print(max_sum)

if __name__ == "__main__" :
  input = sys.stdin.readline
  player_list = []
  c = int(input())

  for _ in range(c) :
    test_case = []
    for _ in range(11) :
      ability = list(map(int, input().split()))
      test_case.append(ability)
    player_list.append(test_case)
  
  find_max(c, player_list)
  
