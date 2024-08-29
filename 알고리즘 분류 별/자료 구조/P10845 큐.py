import sys
from collections import deque

if __name__ == "__main__" :
  input = sys.stdin.readline
  n = int(input())
  queue = deque()

  for _ in range(n) :
    command = input().strip()

    if command.startswith("push") :
      _, num = command.split()
      queue.append(num)
    
    elif command == "pop" :
      if queue :
        print(queue.popleft())
      else :
        print("-1")

    elif command == "size" :
        print(len(queue))

    elif command == "empty" :
      if queue :  # 큐가 비어있지 않다.
        print("0")
      else :
        print("1")

    elif command == "front" :
      if queue :
        print(queue[0])
      else :
        print("-1")

    # command = "back"
    else :
      if queue :
        print(queue[-1])
      else :
        print("-1")
