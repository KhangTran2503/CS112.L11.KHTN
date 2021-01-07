a = [[],[],[]]
s = 0
for i in list(input()):
    a[int(i)%3].append(i)
    s += int(i)
for x in a:
    x.sort(reverse = True)

if s % 3 == 1:
    if len(a[1]) > 0:
        a[1] = a[1][:-1]
    elif len(a[2]) > 1:
        a[2] = a[2][:-2]
if s % 3 == 2:
    if len(a[2]) > 0:
        a[2] = a[2][:-1]
    elif len(a[1]) > 1:
        a[1] = a[1][:-2]

print("".join(sorted(a[0]+a[1]+a[2], reverse = True)))
