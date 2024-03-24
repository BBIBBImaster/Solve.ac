import heapq
import sys

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if self.size() == 0:
            return 0
        else:
            return heapq.heappop(self.heap)

    def size(self):
        return len(self.heap)

if __name__ == "__main__":
    input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline() 사용
    n = int(input())
    min_heap = MinHeap()

    output_buffer = []  # 출력을 모아서 처리하기 위한 버퍼

    for _ in range(n):
        num = int(input())
        if num == 0:
            output_buffer.append(str(min_heap.pop()))  # 출력 버퍼에 추가
        else:
            min_heap.push(num)

    # 출력 버퍼에 있는 결과를 일괄적으로 출력
    sys.stdout.write('\n'.join(output_buffer))
