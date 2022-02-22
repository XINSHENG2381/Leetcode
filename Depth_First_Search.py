### https://www.youtube.com/watch?v=ynZdirmZre4
graph = {
    'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]
}
visited = set()

def dfs(visited,graph,root): #'root' is not accessed
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbor in graph[root]:
            dfs(visited,graph,neighbor)



dfs(visited,graph,'A')
