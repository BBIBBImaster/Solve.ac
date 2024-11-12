def reverse_string(s):
    return s[::-1]

def sort_string(s):
    return ''.join(sorted(s))

def repeat_string(s, n):
    return s * n

def solution(s):
    stack = []
    i = 0
    while i < len(s):
        if s[i] == ')':
            temp = ''
            while stack and stack[-1] != '(':
                temp = stack.pop() + temp
            stack.pop()  # '(' 제거
            
            # 어떤 작업을 할지 확인
            if stack and stack[-1] == 'REVERSE':
                stack.pop()
                temp = reverse_string(temp)
            elif stack and stack[-1] == 'SORT':
                stack.pop()
                temp = sort_string(temp)
            elif stack and stack[-1].startswith('REPEAT'):
                repeat_count = int(stack.pop()[7:-1])
                temp = repeat_string(temp, repeat_count)
            
            for char in temp:
                stack.append(char)
        else:
            # 괄호 또는 일반 문자열 처리
            if s[i] == '(':
                stack.append('(')
            else:
                # 함수나 일반 문자를 스택에 저장
                if s[i:i+7] == 'REVERSE':
                    stack.append('REVERSE')
                    i += 6
                elif s[i:i+4] == 'SORT':
                    stack.append('SORT')
                    i += 3
                elif s[i:i+7] == 'REPEAT(':
                    j = i + 7
                    while s[j] != ')':
                        j += 1
                    stack.append(s[i:j+1])
                    i = j
                else:
                    stack.append(s[i])
        i += 1
    
    return ''.join(stack)

# 테스트 실행
print(solution("REVERSE(SORT(caba)dREPEAT(jpm,3))oz"))  # 기대값: "mpjmpjmpjdcbaaoz"
