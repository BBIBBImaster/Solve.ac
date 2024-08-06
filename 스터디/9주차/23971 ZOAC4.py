import sys

def max_people(h, w, n, m) :
    rows =  (h + n) // (n + 1)
    columns = (w + m) // (m + 1)

    return rows * columns


if __name__ == "__main__" :
    input = sys.stdin.readline
    h, w, n, m = map(int, input().split())
    print(max_people(h,     w, n, m))
