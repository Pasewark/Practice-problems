def check(s,t):
	chardict={}
	for char in s:
		if char in chardict: chardict[char]+=1
		else: chardict[char]=1
	for char in t:
		if char in chardict: 
			chardict[char]-=1
		else: return False
	for key in chardict:
		if chardict[key]!=0: return False
	return True
	
