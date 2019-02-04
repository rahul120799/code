n,a,d=map(int,raw_input().split())
new=0
b=a
for i in range(0,n-1):
	a=a+d
	new=new+a
print (new+b)
