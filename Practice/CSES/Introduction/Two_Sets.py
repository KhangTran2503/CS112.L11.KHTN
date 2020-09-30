n = int(input())
Sum = n*(n+1)/2

if Sum % 2 == 0: 
	Sum = Sum//2
	a = ''
	sum_a = 0
	b = ''
	sum_b = 0

	while (n > 0):
		Sum -= n
		if Sum >= 0:
			a += str(n) + ' '
			sum_a += 1
		else:
			Sum += n
			b += str(n) + ' '
			sum_b += 1
		n -=1 
	print('YES')
	print(sum_a)
	print(a)
	print(sum_b)
	print(b)
else:
	print('NO')         
