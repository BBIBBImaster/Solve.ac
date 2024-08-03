def find_ranking(n, members):
    ranking_list = []

    for i in range(n):
        rank = 1
        for j in range(n):
            if i != j:
                if (int(members[i][0]) < int(members[j][0])) and (int(members[i][1]) < int(members[j][1])):
                    rank += 1
        ranking_list.append(rank)

    answer = ' '.join(map(str, ranking_list))
    return answer

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    members = []
    for _ in range(n):
        member = list(map(int, input().split()))
        members.append(member)

    print(find_ranking(n, members))
