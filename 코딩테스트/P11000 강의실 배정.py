import sys
import heapq

def classroom(n, classes) :
  # 수업을 시작시간 기준으로 정렬
  classes.sort(key=lambda x:x[0])

  # 우선순위 큐 (종료 시간을 저장하는 최소 힙)
  heap = []

  # 첫번째 수업의 종료 시간을 추가
  heapq.heappush(heap, classes[0][1])

  # 두번째 수업시간부터 처리
  for i in range(1,n) :
    # 가장 빨리 끝나는 수업의 종료 시간과 비교
    if classes[i][0] >= heap[0] :
      # 이전 수업이 끝나면 강의실을 재사용할 수 있으므로 pop
      heapq.heappop(heap)

    # 새로운 수업의 종료시간을 힙에 추가
    heapq.heappush(heap, classes[i][1])
    
  return len(heap)

if __name__ == "__main__" :
  input = sys.stdin.readline 
  n = int(input())
  classes = []

  for _ in range(n) :
    si, ti = map(int, input().split())
    classes.append((si, ti))

  print(classroom(n, classes))
