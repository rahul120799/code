n,q=map(int,raw_input().split())
a,b=map(int,raw_input().split())
if n>=a and q>=b:
    print (n-a),(q-b)
elif n<=a and q<=b:
    print (a-n),(b-q)
elif n<=a and q<=b:
    print (n-a),(b-q)
else:
    print (a-n),(q-b)
    
