n, m = map(int, input().split())
edges = {}
for _ in range(m):
    u, v = map(int, input().split())
    try:
        edges[u].append(v)
    except:
        edges[u] = [v]
    try:
        edges[v].append(u)
    except:
        edges[v] = [u]
      
      
visited = set()

def bfs(u):
    index = 0
    queue = [u]
    visited.add(u)  
    
    while index < len(queue):
        u = queue[index]
        index += 1
        if u not in edges:
            continue
        for v in edges[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
        
    return len(queue)
    
ans = []
for i in range(1,n+1):
    if i not in visited:
        ans.append(bfs(i))
print(len(ans) - 1)
anw = 0

if len(ans) > 1:
    base = int(1e9 + 7)
    anw = 1
    anw2 = 1
    for _ in range(len(ans) - 2):
        anw2 = (anw2*n) % base
    for x in ans:
        anw = (anw * x) % base
    anw = anw * anw2 % base
    
print(anw)
