n = int(input())
ans = 0
i = 5
while (n//i >= 1):
	ans += n//i
	i *= 5
print(ans)
	
