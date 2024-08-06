import sys
from collections import deque

def main():
    input = sys.stdin.readline
    # 초기 문자열을 입력받고 deque로 변환
    word = deque(input().strip())
    
    # 명령어의 개수를 입력받음
    m = int(input().strip())
    
    # 커서의 위치를 문자열의 끝으로 설정
    cursor_pos = len(word)
    
    for _ in range(m):
        command = input().strip().split()
        
        if command[0] == 'L':
            if cursor_pos > 0:
                cursor_pos -= 1
        
        elif command[0] == 'D':
            if cursor_pos < len(word):
                cursor_pos += 1
        
        elif command[0] == 'B':
            if cursor_pos > 0:
                word.remove(word[cursor_pos - 1])
                cursor_pos -= 1
        
        elif command[0] == 'P':
            word.insert(cursor_pos, command[1])
            cursor_pos += 1

    # 결과를 출력
    print(''.join(word))

if __name__ == "__main__":
    main()
