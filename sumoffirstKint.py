N=int(raw_input())
K=int(raw_input())
i=0
j=1
b=0
for x in range(0,N):
	if i<=N:
		a=i+1
		i+=1
i=0
for x in range(0,K):
	if i<=K:
		a=i+1
		i+=1
		b+=a
print b


