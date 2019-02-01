num=int(raw_input())
count=0
for d in range(1,num+1):
	if num%d==0:
		count+=1
if count>2:
	print "no"
else:
	print "yes"
