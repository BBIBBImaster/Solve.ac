import sys

if __name__ == "__main__" :
  input = sys.stdin.readline
  t = int(input())

  for _ in range(t) :
    sentence = input().rstrip().split(" ")
    num_word = len(sentence)
    for i in range(num_word) :
      print(sentence[i][::-1], end = " ")