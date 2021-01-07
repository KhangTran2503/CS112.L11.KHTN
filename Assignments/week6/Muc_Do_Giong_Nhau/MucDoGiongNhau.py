str1 = input()
str2 = input()

dct2 = {}
for i in range(len(str2)-1):
	s = str2[i:i+2]
	try:
		dct2[s] += 1
	except:
		dct2[s] = 1

ans = 0
for i in range(len(str1)-1):
	s = str1[i:i+2]
	if s in dct2:
		ans += 1
	
print(ans)
	
