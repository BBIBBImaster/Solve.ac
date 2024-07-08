import sys

def solution(numbers, target):
    def dfs(index, current_sum) :
        # 모든 숫자를 다 사용한 경우,
        if index  == len(numbers) :
            # 합이 타겟과 같으면
            if current_sum == target :
                return 1
            else :
                return 0
        
        add = dfs(index + 1, current_sum + numbers[index])
        subtract = dfs(index + 1, current_sum - numbers[index])

        return add + subtract
    return dfs(0,0)

if __name__ == "__main__":
    input = sys.stdin.readline
    numbers = list(map(int, input().strip().split()))
    target = int(input().strip())
    
    print(solution(numbers, target))