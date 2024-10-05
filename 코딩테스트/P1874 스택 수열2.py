import sys

def find_answer(target_list) :
  stack = []
  result = []
  current = 1

  for num in target_list :
    while current <= num :
      stack.append(current)
      current += 1
      result.append("+")
      
    if stack[-1] == num :
      stack.pop()
      result.append("-")

    else :
      return "NO"

  return result

if __name__ == "__main__" :
  input = sys.stdin.readline
  n = int(input())
  target_list = []

  for _ in range(n) :
    num = int(input())
    target_list.append(num)

  result = find_answer(target_list)

  if result == "NO":
     print(result)
  else:
    for operation in result:
      print(operation)