val=raw_input()
exp=['a','e','i','o','u']
if val.isdigit():
	print "invalid"
elif val.isalpha():
	for x in exp:
		if x==val:
			print "Vowel"
	else:
		print "Consonant"
