import sys
import heapq

input = sys.stdin.readline

def min_heap(commands):
    heap = []
    
    for cmd in commands:
        if cmd == 0:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, cmd)

if __name__ == "__main__":
    n = int(input())
    commands = [int(input()) for _ in range(n)]
    min_heap(commands)
