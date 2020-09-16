'''
    @author: I_Love_Thuy_Linh
    Link   : https://projecteuler.net/problem=28
    
    Trick  : ???

'''

dx = [1,1,-1,-1]
dy = [1,-1,-1,1]

num = [[1] for _ in range(4)]

for i in range(0,1001//2):
    for j in range(4):
        delta = 2*(4*i + j + 1)
        num[j].append(num[j][-1] + delta)

ans = 1
for i in range(4):
    ans += sum(num[i][1:])

print(ans)
