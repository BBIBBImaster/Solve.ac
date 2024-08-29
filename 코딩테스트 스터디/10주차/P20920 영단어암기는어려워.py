import sys
from collections import Counter

def filtering_word(n, m, word_list) :
  filtered_list = [word for word in word_list if len(word) >= m]

  word_count = Counter(filtered_list)

  # 기존 코드
  # # 알파벳 오름차순 정렬
  # sorted_by_alpha = sorted(filtered_list)

  # # 길이 내림차순 정렬
  # sorted_by_length = sorted(sorted_by_alpha, key=len, reverse=True)

  # # 빈도 내림차순 정렬
  # sorted_by_frequency = sorted(sorted_by_length, key=lambda word: word_count[word], reverse=True)

  # # 중복 제거
  # answer = []
  # for word in sorted_by_frequency :
  #   if word not in answer  :
  #     answer.append(word)

  # 새 코드
  # 우선순위에 따라 정렬: (빈도 내림차순, 길이 내림차순, 알파벳 오름차순)
  sorted_words = sorted(word_count.keys(), key=lambda word: (-word_count[word], -len(word), word))

  return sorted_words

if __name__ == "__main__" :
  input = sys.stdin.readline
  word_list = []

  n, m = map(int, input().split())
  for _ in range(n) :
    word = str(input().strip())
    word_list.append(word)

  answer = filtering_word(n, m, word_list)

  for i in range(len(answer)) :
    print(answer[i])

