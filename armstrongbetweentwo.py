N,Q=map(int,raw_input().split())
for num in range(N+1,Q):
    num1=list(str(num))
    l=len(num1)
    new=0
    val=0
    j=0
    for i in num1:
    	new=int(i)**l
    	val+=new
    if val==int(num):
     print val,
   
	
