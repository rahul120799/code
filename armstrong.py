num=raw_input()
num1=list(num)
l=len(num1)
new=0
val=0
j=0
for i in num1:
	new=int(i)**l
	val+=new
if val==int(num):
    print "yes"
else:
    print "no"
	
