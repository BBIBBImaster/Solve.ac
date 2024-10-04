import sys
input = sys.stdin.readline

# 스위치의 개수
num_switch = int( input() )
# 스위치의 상태 -> 계속 변환할 것
list_switch = list(map(int, input().split()))
# 학생의 수
num_student = int(input())  
# 학생의 성별(남:1, 여:2) / 받은 스위치  수
list_student = [list(map(int, input().split())) for _ in range(num_student)]

def change_switch(list_switch, gender, switch_num) :
    if gender == 1 :
        # 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
        for i in range(switch_num, num_switch + 1, switch_num) :
            list_switch[i-1] = 1 - list_switch[i-1]
    else : 
        # 일단 해당 스위치 변경
        list_switch[switch_num-1] = 1 - list_switch[switch_num-1]
        # 좌우 대칭인지 확인
        left = right = switch_num - 1
        while ( left >= 0 ) and ( right <= num_switch -1 ) and ( list_switch[left] == list_switch[right] ) :
            list_switch[left] = 1 - list_switch[left]
            list_switch[right] = 1 - list_switch[right]
            left -= 1
            right += 1

    return list_switch

for gender, switch_num in list_student :
    change_switch(list_switch, gender, switch_num)

# 최종 스위치 상태 출력
for i in range(num_switch):
    print(list_switch[i], end=" ")
    # 한 줄에 20개씩 출력하도록 처리
    if (i + 1) % 20 == 0:
        print()
# 마지막 줄에 줄 바꿈 추가 rkdan
if num_switch % 20 != 0:
    print()

