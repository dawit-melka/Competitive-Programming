n = int(input())
indegree = [0]*n
outdegree = [0]*n

for i in range(n):
    
    curr = list(map(int, input().split()))
    
    for j in range(n):
        outdegree[i] += curr[j]
        indegree[j] += curr[j]
   
sources = []
sinks = []

for i in range(n):
    if indegree[i] == 0:
        sources.append(i + 1)
    if outdegree[i] == 0:
        sinks.append(i + 1)

print(len(sources),*sources)
print(len(sinks),*sinks)
