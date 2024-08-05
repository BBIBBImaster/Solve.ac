import sys

def editor(word, cmds) :
  cursor_pos = len(word)

  for cmd in cmds :
    # 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
    if cmd[0] == "L" :
      if cursor_pos > 0 :
        cursor_pos -= 1

    # 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
    elif cmd[0] == "D" :
      if cursor_pos < len(word) :
        cursor_pos += 1

    # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    elif cmd[0] == "B" :
      if cursor_pos > 0 :
         word = word[:cursor_pos-1] + word[cursor_pos:]
         cursor_pos -= 1

    # '$'라는 문자를 커서 왼쪽에 추가함
    else :
      word = word[:cursor_pos] + cmd[1] + word[cursor_pos:]
      cursor_pos += 1

  return word

if __name__ == "__main__" :
  input = sys.stdin.readline
  word = str(input())
  n = int(input())

  for _ in range(n) :
    cmds = list(map(str, input().split()))
    editor(word, cmds)

  print(word)