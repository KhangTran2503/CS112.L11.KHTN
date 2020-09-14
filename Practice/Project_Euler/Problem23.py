'''
    @author: I_Love_Thuy_Linh
    Link: https://projecteuler.net/problem=23
'''

cnt = [0]*28124
for i in range(1,28124//2):
    for j in range(i + i,28124,i):
        cnt[j] += i

ans = 0
#cnt_abundant = [0]*28214
cnt_ans = 0
abundant = []
for i in range(1,28124):
    if cnt[i] > i:
        abundant.append(i)


is2_abundant = [0]*28124
for i in range(len(abundant)):
    j = i
    while j < len(abundant) and abundant[i] + abundant[j] < 28124:
        is2_abundant[abundant[i] + abundant[j]] = 1
        j += 1

exclusive_ans = 0
for i in range(1,28124):
    if is2_abundant[i] == 1:
        print(i)
        exclusive_ans += i

ans = (28124//2)*28123 - exclusive_ans

print(ans)




