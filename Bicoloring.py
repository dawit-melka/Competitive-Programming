def solve(n, m):

    adj = {}
    colors = [-1]*(n+1)
    for _ in range(m):
        n1, n2 = map(int, input().split())
        if n1 not in adj:
            adj[n1] = []
        if n2 not in adj:
            adj[n2] = []
        
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    def dfs(parentClr, index):
        if parentClr == colors[index]:
            return False
        if colors[index] != -1:
            return True
        if index not in adj:
            return True
        colors[index] = (1+parentClr)%2
        for child in adj[index]:
            if not dfs(colors[index], child):
                return False
        return True
        
    for i in range(1, n+1):
        if colors[i] == -1:
            if not dfs(3, i):
                return False
    return True
while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    if solve(n, m):
        print('BICOLOURABLE.')
    else:
        print("NOT BICOLOURABLE.")
