from collections import deque

# 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
def playing_card(n) :
  card_deque = deque(range(1, n + 1))

  while len(card_deque) > 1 :
    card_deque.popleft() # 제일 위의 카드를 버림
    card_deque.append(card_deque.popleft())

  return card_deque[0]

if __name__ == "__main__" :
  import sys
  input = sys.stdin.readline
  n = int(input())
  
  print(playing_card(n))