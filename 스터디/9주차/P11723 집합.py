import sys

S = set()

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

def aggregation(cmd, num):
    global S  # 전역 변수 S를 사용하기 위해 선언

    if cmd == "add":
        S.add(num)
    elif cmd == "remove":
        S.discard(num)
    elif cmd == "check":
        print(1 if num in S else 0)
    elif cmd == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif cmd == "all":
        S = set(range(1, 21))
    elif cmd == "empty":
        S.clear()

if __name__ == "__main__" :
  input = sys.stdin.readline
  m = int(input())
  for _ in range(m) :
    cmd = input().split()
    if len(cmd) == 2 :
      aggregation(cmd[0], int(cmd[1]))
    else :
      aggregation(cmd[0], None)  