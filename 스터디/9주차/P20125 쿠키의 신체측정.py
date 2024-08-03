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
    left_arm_candidate = graph[i+1][0: j]
    for k in range(len(left_arm_candidate)) :
        if left_arm_candidate[k] == "*" :
            left_arm += 1
  
    right_arm = 0
    right_arm_candidate = graph[i+1][j+1 : n]
    for k in range(len(right_arm_candidate)) :
        if right_arm_candidate[k] == "*" :
            right_arm += 1

    waist = 0
    waist_candidate = graph[i + 2][j]
    while waist_candidate == '*' :
        waist += 1
        if i + 2 + waist < n:
            waist_candidate = graph[i + 2 + waist][j]
        else:
            break
  
        
    left_leg = 0
    left_leg_candidate = graph[i + 2 + waist][j-1]
    while left_leg_candidate == '*' :
        left_leg += 1
        if i + 2 + waist + left_leg < n :
            left_leg_candidate = graph[i+ 2 + waist + left_leg][j-1]
        else :
            break

    right_leg = 0
    right_leg_candidate = graph[i + 2 + waist][j+1]
    while right_leg_candidate == '*' :
        right_leg += 1
        if i + 2 + waist + right_leg < n :
            right_leg_candidate = graph[i+ 2 + waist + right_leg][j+1]
        else :
            break

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