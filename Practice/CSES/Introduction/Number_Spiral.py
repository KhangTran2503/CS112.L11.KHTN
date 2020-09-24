n = int(input())

for i in range(n):
	a,b = map(int, input().split())
	if a >= b:
		if a % 2 == 1:
			print((a-1)**2 + b)
		else:
			print(a**2 - b + 1)
	else:
		if b % 2 == 1:
			print(b**2 - a + 1)
		else:
			print((b-1)**2 +a)
