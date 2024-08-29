import sys

input = sys.stdin.readline

class Stack :
    def __init__(self):
        self.item = []

    def push(self, n) :
        self.item.append(n)

    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
    # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop(self) :
        if len(self.item) == 0 :
            return -1
        else :
            return self.item.pop()


    def size(self) :
        return len(self.item)

    def empty(self) :
        if len(self.item) == 0 :
            return 1
        else :
            return 0

    def top(self) :
        if len(self.item) == 0 :
            return -1
        else :
            return self.item[-1]


# 메인 함수
S = Stack()

n = int(input())
for _ in range(n) :
    command = list(map(str, input().split()))

    # command의 length가 2면, push일 것.
    if len(command) == 2 :
        S.push(command[1])

    else :
        if command[0] == "pop" :
            print(S.pop())

        elif command[0] == "size" :
            print(S.size())

        elif command[0] == "empty" :
            print(S.empty())

        else :      # command가 top일 경우,
            print(S.top())