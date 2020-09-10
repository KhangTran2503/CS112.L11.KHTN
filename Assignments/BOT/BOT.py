n = int(input())
a = list(map(int,input().split()))

premin = 0
Sum = 0
MaxSum = -1000000000000000000
prep = 0


for i in range(n):
    Sum += a[i]

    if Sum - premin > MaxSum:
        ansp = prep
        ansq = i + 1
        MaxSum = Sum - premin
    if Sum < premin:
        premin = Sum
        prep = i + 1

print(ansp + 1,ansq,MaxSum,end=' ')

