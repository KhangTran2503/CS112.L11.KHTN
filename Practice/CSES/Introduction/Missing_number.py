n = int(input())
l = list(map(int,input().split()))

Sum = n*(n+1)//2
sum_list = sum(l)

print(Sum - sum_list)
