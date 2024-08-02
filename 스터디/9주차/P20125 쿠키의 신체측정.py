def find_length(n, graph):
    found = False

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '*':
                  found = True
                  heart_x, heart_y = i + 2, j + 1
                  break
        if found :
            break
    
    left_arm = 0
    right_arm = 0
    waist = 0
    left_leg = 0
    right_leg = 0

    return heart_x, heart_y, left_arm, right_arm, waist, left_leg, right_leg


if __name__ == "__main__" :
  import sys
  input = sys.stdin.read
  data = input().splitlines()

  n = int(data[0])
  graph = []
  for i in range(1, n+1) :
    graph.append(data[i])

  heart_x, heart_y, left_arm, right_arm, waist, left_leg, right_leg = find_length(n, graph)
  print(heart_x, heart_y)
  print(left_arm, right_arm, waist, left_leg, right_leg)