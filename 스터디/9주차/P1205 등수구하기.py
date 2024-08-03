
def insert_ranking(n, new, p, numbers) :

  if n == 0 :
    return 1
  
  # 들어갈 자리가 있을 경우,
  elif (p-n >= 1) :
    numbers.append(new)
    numbers.sort(reverse = True)
    return int(numbers.index(new)) + 1

  # 랭킹에 들어갈 자리가 없을 경우,
  else :
    numbers.sort(reverse = True)
    if numbers[len(numbers)-1] >= new :
      return -1
    else :
      numbers.append(new)
      numbers.sort(reverse = True)
      return int(numbers.index(new)) + 1
  
if __name__ == "__main__" :
  import sys
  input = sys.stdin.readline
  n, new, p = map(int, input().split())
  numbers = list(map(int, input().split()))

  print(insert_ranking(n, new, p, numbers))


