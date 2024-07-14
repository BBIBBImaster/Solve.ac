import sys
input = sys.stdin.readline

def find_password(s, p, dna, condition):
    count = 0
    candidates = []

    for i in range(s - p + 1):
        candidate.append(dna[i:i + p])

    for candidate in candidates:
        a_count = candidate.count('A')
        c_count = candidate.count('C')
        g_count = candidate.count('G')
        t_count = candidate.count('T')

        if (a_count >= condition[0] and 
            c_count >= condition[1] and 
            g_count >= condition[2] and 
            t_count >= condition[3]):
            count += 1
    
    print(count)

if __name__ == "__main__":
    s, p = map(int, input().split())
    dna = input().strip()
    # [A, C, G, T]
    condition = list(map(int, input().split()))

    find_password(s, p, dna, condition)
