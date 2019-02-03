num1,num=map(int,raw_input().split())
count=0
for x in range(num1+1,num):
	for y in range(1,num+1):
		if x%y==0:
			count+=1
	if count==2:
		print x,
	count=0
