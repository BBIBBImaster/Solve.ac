import sys

if __name__ == "__main__" :
  input = sys.stdin.readline
  n = int(input())

  num_list = list(map(int, input().split()))
  num_list.sort()

  if len(num_list) == 1:
    print(num_list[0] * num_list[0] )
  else :
    print(num_list[0] * num_list[n-1])