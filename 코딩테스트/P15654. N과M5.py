import sys
from itertools import permutations

if __name__ == "__main__" :
  input = sys.stdin.readline
  n, m = map(int, input().split())

  num_list = list(map(int, input().split()))
  num_list.sort()

  for perm in permutations(num_list, m) :
    print(' '.join(map(str, perm)))
    

  