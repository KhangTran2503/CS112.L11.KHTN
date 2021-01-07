a = input()

length = len(a)
ans = 1
temp = 1
for i in range(1,length):
	ans = max(ans,temp)
	if a[i] == a[i - 1]:
		temp += 1
	else:
		temp = 1
	ans = max(ans,temp) 
print(ans)
