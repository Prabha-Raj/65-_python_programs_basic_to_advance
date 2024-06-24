#gratest finder

def  greatest(a,b,c):
	if a>b and a>c:
		return(a)
	elif b>c and b>a:
		return(b)
	else:
		return(c)
a=int(input("Enter first Number  : "))
b=int(input("Enter Second Number : "))
c=int(input("Enter Third Number : "))
print("The Greatest Number is  :  ",greatest(a,b,c))