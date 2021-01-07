from math import gcd
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a*d < b*c:
    cnt = 0
    while (a*d <= b*c):
        g = gcd(a + 1,b + 1)
        a = (a + 1)//g
        b = (b + 1)//g
        cnt += 1
        if (a == c and b == d):
            print(cnt)
            quit()

print(0)
