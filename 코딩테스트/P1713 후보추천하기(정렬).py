n = int(input())
a = int(input())
process = list(map(int, input().split()))


class Candidate:
    def __init__(self,num):
        self.num = num
        self.recommendationCount = 0
        self.timeStamp = 0

    def voted(self):
        self.recommendationCount =+ 1

    def time(self):
        self.timeStamp =+ 1

class Frame:
    def __init__(self,capacity):
        self.capacity = capacity
        self.candidates = []


if __name__ == "__main__":
    # 사진틀 생성
    frame = Frame(n)

    # 추천 과정
    for i in range(process):
        Candidate(i)






