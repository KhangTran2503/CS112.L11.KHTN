from sys import stdin, stdout

s = stdin.readline().strip()

n = len(s)
H = [0]

def gen_hash(c):
    return ord(c)**3
def get_hash(l,r):
    return H[r]-H[l-1]

for c in s:
    H.append(H[-1]+gen_hash(c))

p = int(input())
for _ in range(p):
    a,b,c,d = map(int, stdin.readline().split())
    if get_hash(a,b)==get_hash(c,d):
        print("YES")
    else:
        print("NO")
