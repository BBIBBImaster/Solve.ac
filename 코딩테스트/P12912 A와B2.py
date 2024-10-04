def is_possible(s, t):
    if len(t) < len(s):
        return False
    
    if s == t:
        return True
    
    # t의 마지막 문자가 'A'이면, 마지막 'A'를 제거하고 재귀 호출
    if t[-1] == 'A':
        if is_possible(s, t[:-1]):
            return True
    
    # t의 첫 번째 문자가 'B'이면, 문자열을 뒤집고 첫 번째 'B'를 제거하고 재귀 호출
    if t[0] == 'B':
        reversed_t = t[::-1]
        if is_possible(s, reversed_t[:-1]):
            return True
    
    # 어느 조건도 만족하지 않으면 불가능
    return False

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    s = input().strip()
    t = input().strip()

    if is_possible(s, t):
        print(1)
    else:
        print(0)
