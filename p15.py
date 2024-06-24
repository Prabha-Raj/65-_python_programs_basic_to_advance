#Ladder statement

a=eval(input("Enter first Number : "))
b=eval(input("Enter second Number : "))
c=eval(input("Enter Third Number : "))
if a>b and a>c:
	print("A is Greater")
elif b>c and b>a:
	print("B is Greater")
else:
	print("C is Greater")