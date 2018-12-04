#this is the DFS algorithms for no weights graph


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
		 
		 
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print(list(dfs_paths(graph, 'A', 'F')), "The first one is the shortest path for no edge weights graph") # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
print(dfs_paths(graph, 'A', 'F'))

