"""
    @author: I_Love_Thuy_Linh

    Reference: https://www.geeksforgeeks.org/find-length-period-decimal-value-1n/

"""
from collections import defaultdict

def getPeriod(n):
    rem = 1
    curpos = 1
    mymap = defaultdict(int)

    while 1:
        rem = (rem * 10) % n
        if rem == 0: return curpos
        prepos = mymap[rem]
        if prepos > 0:
            return curpos - prepos

        mymap[rem] = curpos
        curpos += 1


max_period = 0
ans = 0
for x in range(1,1000):
    cur_period = getPeriod(x)
    if cur_period > max_period:
        ans = x
        max_period = cur_period

print(ans)


#print(getPeriod(7))
