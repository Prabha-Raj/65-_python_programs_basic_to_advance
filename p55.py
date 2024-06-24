#EH
try:
	a=int(input("Enter first Number : "))
	b=int(input("Enter Second Number : "))
	c=a/b
	print("Division = ",c)
except ValueError:
	print("Please Enter Integer Value ")
except ZeroDivisionError:
	print("Number is Not Divisible by Zero ")
finally:
	print("I Love Rohit Sir ")