import sys

input = sys.stdin.readline

def check(nlist) :
    length = len(nlist)
    half = int(length / 2)
    front_list = nlist[:half]

    # 만약, 리스트의 길이가 홀수라면, 중앙의 숫자는 무시
    if length % 2 == 0:
        back_list = nlist[half:]
    else :
        back_list = nlist[half+1:]

    back_list_reverse = list(reversed(back_list))

    if front_list == back_list_reverse :
        return "yes"
    else :
        return "no"

while True :
    n = list(map(int, input().rstrip()))

    # 입력이 0일 경우, break
    if (len(n)==1) and n[0]==0 :
        break

    print(check(n))

