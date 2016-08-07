l=raw_input()
co=0
for i in range(len(l)+1):
	for j in range(len(l)+1):
		if i>j:
			t=l[j:i]
			if t==t[::-1]:
				#print t  #this statement prints unique substring palindromes
				co=co+1
print co   #count of palindrome substrings

			
