#Simle calculator using function.

def sum(a,b):
	return(a+b)
def sub(a,b):
	return(a-b)
def div(a,b):
	return(a//b)
def multi(a,b):
	return(a*b)
def rem(a,b):
	return(a%b)
def power(a,b):
	return(a**b)
def sq(a):
	return(a*a)
def cube(a):
	return(a*a*a)
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
print("Sum = ",sum(num1,num2))
print("Sub = ",sub(num1,num2))
print("Div = ",div(num1,num2))
print("Multi = ",multi(num1,num2))
print("Rem = ",rem(num1,num2))
print("Power = ",power(num1,num2))
print("Square of First number = ",sq(num1))
print("Cube of Second Number = ",cube(num2))

