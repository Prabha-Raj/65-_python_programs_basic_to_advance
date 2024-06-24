#fibbonacci 
'''
num=int(input("How many terms you want to print : "))
term1=0
term2=1
print(term1)
print(term2)
for i in range(1,(num-1)):
	next_term=term1+term2
	print(next_term)
	term1=term2
	term2=next_term
'''


num=int(input("How many terms you want to print : "))
term1=0
term2=1
print(term1,term2,end=" ")
for i in range(1,(num-1)):
	next_term=term1+term2
	print(next_term,end=" ")
	term1=term2
	term2=next_term
