def solve():
    N = int(input())  # 채널 수
    channels = [input().strip() for _ in range(N)]  # 채널 리스트

    result = []

    # KBS1을 첫 번째로 이동시키기
    kbs1_idx = channels.index("KBS1")
    for _ in range(kbs1_idx):  # KBS1 위치까지 화살표를 아래로 이동
        result.append("1")
    for _ in range(kbs1_idx):  # KBS1을 첫 번째로 올림
        result.append("4")

    # KBS2를 두 번째로 이동시키기
    kbs2_idx = channels.index("KBS2")  # KBS1이 이미 첫 번째로 갔으니 KBS2의 인덱스가 변함
    if kbs2_idx > 1:
        for _ in range(kbs2_idx - 1):  # KBS2 위치까지 화살표를 아래로 이동
            result.append("1")
        for _ in range(kbs2_idx - 1):  # KBS2를 두 번째로 올림
            result.append("4")

    # 결과 출력
    print(''.join(result))

if __name__ == "__main__":
    solve()
