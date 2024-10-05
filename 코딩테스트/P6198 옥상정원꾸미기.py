import sys

# def count(n, b_list) :
#   count_list = []
  
#   for i in range(n-1) :
#     count = 0
#     for j in range(i+1, n) :
#       if b_list[j] < b_list[i] :
#         count += 1
#       elif b_list[j] >= b_list[i] :
#         break
#     count_list.append(count)
    
#   count_list.append(0)

#   return sum(count_list)

def count(n, b_list) :
  stack = []
  count = 0

  for i in range(n) :
    while stack and stack[-1] <= b_list[i] :
      stack.pop()

    count += len(stack)

    stack.append(b_list[i])
    
  return count

if __name__ == "__main__" :
  input = sys.stdin.readline
  b_list = []

  n = int(input())
  for _ in range(n) :
    b = int(input())
    b_list.append(b)
  
  print(count(n, b_list))

