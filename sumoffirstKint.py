c=int(input("Enter number:"))
if(c<1 or (c%1)!=0):
    print("wrong input")
else:
    temp=0
    while(n!=0):
        temp=temp+c
        c=c-1
    print (temp)
