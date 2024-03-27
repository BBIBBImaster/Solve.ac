import sys
input = sys.stdin.readline

# 스위치의 개수
num_switch = int(input())
# 스위치의 상태
list_switch = map(int, input().split())
# 학생의 수
num_student = int(input())
# 학생의 성별(남:1, 여:2) / 받은 스위치  수
list_student = [list(map(int, input().split()) for _ in range(num_student))]

# for i in range(len(list_student)) :
#     # 남자면, 
#     if list[i][0] == 1 :
#         print("남자")
#     else :
#         print("여자")

for i in range(len(list_student)) :
    print(list_student[i])
