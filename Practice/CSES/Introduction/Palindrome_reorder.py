def palindromeRearranging(inputString):
	elements = {c:inputString.count(c) for c in set(inputString)}
	#print(elements)
	even = [e % 2 == 0 for e in elements.values()]
	#print(even)
	#print(all(even))
	a = ['0']*len(inputString)
	if all(even):
		
	elif (len(inputString) % 2 == 1 and even.count(False) == 1):
	else:
		print('NO SOLUTION')

def main():
	inputString = input()
	print(palindromeRearranging(inputString))

if __name__=='__main__':
	main()
