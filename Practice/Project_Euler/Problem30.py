'''
    @author: I_Love_Thuy_Linh
    Link   : https://projecteuler.net/problem=30
'''
low = 2
high = 10**6

ans = 0
for x in range(low,high):
    sum_fifth_pow = 0
    for c in str(x):
        sum_fifth_pow += int(c)**5
    if x == sum_fifth_pow:
        print(x)
        ans += x

print(ans)


