import sys

l = int(sys.stdin.readline())
word = sys.stdin.readline()
result = 0

for i in range(len(word)-1) :
    result += (ord(word[i]) - ord('a')+1) * (31 ** i)

print(result)
