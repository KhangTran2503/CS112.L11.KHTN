import random
import os

NAME = "DIALAN"
MAX = (1<<12) - 1

YES = 0
NO = 0

def gen_array(n):
	ans = []
	for i in range(n):
		if random.random() < 0.0001:
			ans.append(random.randrange(MAX))
		else:
			ans.append(random.choice([1,3,7,15,31,63,127,255,511,1023,2047,4095]))
	return ans

def solve(n, k, a):

	def number_bit_zero(x,mask):
		cnt = 0
		for pos in range(12):
			if (x >> pos) & 1 == 0 and (mask >> pos) & 1 == 1:
				cnt += 1
		return cnt


	#choose = [0 for _ in range(n)]
	mask = (1 << 12) - 1

	cnt = 0
	for pos in range(12):
		if (mask >> pos) & 1 == 1:
			tmp = -1
			for x in a:
				if (x >> pos) & 1 == 0 :
					#print(x)
					#print('------------------------------')
					tmp_zero = number_bit_zero(mask & x,mask)
			#print(tmp_zero)
					if tmp_zero > tmp:
						tmp = tmp_zero
						arg = x
			if (tmp == -1):
				return False
			cnt += 1
			mask &= arg
		#print(mask)
			if (mask == 0): break

	if cnt <= k:
		return True
	else:
		return False

def write_test(index, n, k, array):
	print(index)
	global YES
	global NO
	dirname = NAME + str(index).zfill(3)
	if not os.path.exists(dirname):
		os.mkdir(dirname)

	filepath = os.path.join(dirname, NAME)
	with open(filepath + ".INP", "w") as f:
		f.write("{} {}\n".format(n,k))
		for x in array:
			f.write("{} ".format(x))

	with open(filepath + ".OUT", "w") as f:
		if solve(n,k,array):
			f.write("YES")
			YES+=1
		else:
			f.write("NO")
			NO+=1

index = 0
for n in range(1, 20000,100):
	index += 1
	k = random.randint(1,max(2, min(100,n//256)))
	array = gen_array(n)
	write_test(index, n, k, array)

print(YES, NO)