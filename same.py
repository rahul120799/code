N=int(raw_input())
a=raw_input()
b=raw_input()
c=list(a)
d=list(b)
e=len(c)
f=len(d)
if e>=f:
	for x in range(0,e):
		for y in range(0,f):
			if c[x]==d[y]:
				print c[y],
else:
	for x in range(0,f):
		for y in range(0,e):
			if d[x]==c[y]:
				print d[x],
