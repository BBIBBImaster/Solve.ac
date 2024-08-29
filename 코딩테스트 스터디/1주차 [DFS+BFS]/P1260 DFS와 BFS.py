import sys
from collections import deque

def create_graph(n, edges) :
    graph = {}

    for i in range(1, n+1) :
        graph[i] = []

    for edge in edges :
        v1, v2 = edge
        graph[v1].append(v2)
        graph[v2].append(v1)

    return graph

def DFS(graph, start) :
    visited = set()
    stack = [start]
    result = []

    while stack : 
        vertex = stack.pop()
        if vertex not in visited :
            visited.add(vertex)
            result.append(vertex)
            stack.extend(sorted(graph[vertex], reverse=True))
        
    return result

def BFS(graph, start) :
    visited = set()
    queue = deque([start])
    result = []

    while queue :
        vertex = queue.popleft()
        if vertex not in visited :
            visited.add(vertex)
            result.append(vertex)
            queue.extend(sorted(graph[vertex]))

    return result

n, m, v = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = create_graph(n, edges)
print(graph)
print(DFS(graph, v))
print(BFS(graph, v))
