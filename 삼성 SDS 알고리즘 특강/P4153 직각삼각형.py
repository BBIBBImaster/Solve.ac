#마지막줄에는 0 0 0이 입력된다.

while True:
    a, b, c = map(int,input().split())

    if (a==0) and (b==0) and (c==0):
        break

    numList = []
    numList.append(a)
    numList.append(b)
    numList.append(c)

    numList.sort()
    if (numList[-1] * numList[-1]) == ((numList[0]) * (numList[0])) + ((numList[1]) * (numList[1])):
        print("right")
    else:
        print("wrong")

