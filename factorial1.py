num=int(raw_input())
i=1
new=1
if num==0:
    print new
else:
    for i in range(1,num+1):
        new*=i
    print new
