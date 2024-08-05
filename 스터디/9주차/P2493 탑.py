import sys

# 기존코드 (시간초과)
# def receive_tower(n, tower_list) :
#     check_list = []
#     answer_list = []

#     for i in range(n) :
#         if len(check_list) == 0 :
#             answer_list.append(0)
#         else:
#             found = False
#             for j in range(len(check_list) - 1, -1, -1):
#                 if tower_list[i] <= check_list[j]:
#                     answer_list.append(j + 1)
#                     found = True
#                     break
#             if not found:
#                 answer_list.append(0)

#         check_list.append(tower_list[i])

#     return answer_list

# 고친 코드 (Stack 사용)
def receive_tower(n, tower_list):
    stack = []
    answer_list = [0] * n

    for i in range(n):
        while stack and tower_list[stack[-1]] <= tower_list[i]:
            stack.pop()
        
        if stack:
            answer_list[i] = stack[-1] + 1
        
        stack.append(i)

    return answer_list

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    tower_list = list(map(int, input().split(" ")))

    print(' '.join(map(str, receive_tower(n, tower_list))))