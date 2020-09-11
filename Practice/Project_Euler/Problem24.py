import itertools

perm = list(itertools.permutations([str(x) for x in range(10)]))

print(''.join(perm[1000000 - 1]))

