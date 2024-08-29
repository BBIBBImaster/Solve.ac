import sys

def hearthStone(num) :
  num = num % 6
  if num == 1 :
    return "SK"
  elif num == 2:
    return "CY"
  elif num == 3:
    return "SK"
  elif num == 4:
    return "CY"
  elif num == 5:
    return "SK"
  else :
    return "CY"

if __name__ == "__main__" :
  input = sys.stdin.readline
  n = int(input())
  print(hearthStone(n))


