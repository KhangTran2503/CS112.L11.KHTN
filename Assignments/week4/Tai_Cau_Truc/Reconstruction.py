import sys
sys.setrecursionlimit(500001)
n, m = map(int, input().split())
edges = {}
for _ in range(m):
    u, v = map(int, input().split())
    try:
        edges[u].append(v)
    except:
        edges[u] = [v]

color = [0 for _ in range(n + 1)]
topo = []


"""
    Check cycle in graph
"""
def check_cycle(u):
    color[u] = 1
    if u in edges:
        for v in edges[u]:
            if color[v] == 0:
                if check_cycle(v): return True
            else:
                if color[v] == 1:
                    return True
                    
    color[u] = 2
    topo.append(u)
    return False


for u in range(1,n + 1):
    if color[u] == 0:
        if check_cycle(u):
            print('No')
            quit()

'''
    dfs check cross arc and root
'''

par = [-1 for _ in range(n + 1)]
for u in topo:
    if u in edges:
        for v in edges[u]:
            if par[v] == -1:
                par[v] = u
'''
    Check graph have one root
'''
root = -1
for u in range(1,n + 1):
    if par[u] == -1:
        if root != -1: # have two root
            print('No')
            quit()
        root = u
'''
    dfs
'''
time_in = [0 for _ in range(n + 1)]
time_out = [0 for _ in range(n + 1)]

time = 0
def dfs(u):
    global time
    time += 1
    time_in[u] = time
    if u in edges:
        for v in edges[u]:
            if time_in[v] == 0:
                dfs(v)
    time += 1
    time_out[u] = time

dfs(root)
#print(time_in)
#print(time_out)
for u in range(1,n + 1):
    if u in edges:
        for v in edges[u]:
            if not (time_in[u] <= time_in[v] and time_out[u] >= time_out[v]):
               # print(u,v)
                print('No')
                quit()

print('Yes')
for u in range(1,n + 1):
    print(par[u],end=' ')

