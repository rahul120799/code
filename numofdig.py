user=int(raw_input())
if user<=9 and user>=0:
	print "1"
elif user<=99 and user>=10:
	print "2"
elif user<=999 and user>=100:
	print "3"
elif user<=1000 and user>=9999:
	print "4"
else:
	print "5"
