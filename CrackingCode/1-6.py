def compress(s):
	current=[s[0],1]
	t=''
	for i in xrange(1,len(s)):
		if s[i]!=current[0]:
			t=t+str(current[1])+current[0]
			current=[s[i],1]
		else:
			current[1]+=1
	t=t+str(current[1])+current[0]
	if len(t)<len(s):return t
	return s
	
