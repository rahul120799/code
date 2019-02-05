a=raw_input()
i=0
try:
    float(a)
    i+=1
    print "yes"
except ValueError:
    pass
if i<1:
    if a.isdigit():
        print "yes"
    else:
        print "No"

