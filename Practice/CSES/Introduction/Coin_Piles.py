n = int(input())
#from  math import abs
for i in range(n):
	a, b = map(int, input().split())
	if ((a + b) % 3 == 0):
		if((a+b) //3 >= abs(a-b)):
			print('YES')
		else:
			print('NO')
	else:
		print('NO')
