'''
Write a python program to create a module named tempconv. 
In tempconv module create two function ctof() and ftoc(). 
ctof() function converts temperature from centigrade to 
Fahrenheit  and ftoc() function converts temperature from 
Fahrenheit to centigrade. Now import tempconv module 
and test ctof() and ftoc() functions.
'''
import tempconv
choice=int(input("Enter 1 for C to F and 2  F to C : "))
if choice==1:
	c=eval(input("Enter Temprature in C : ",))
	print("Temprature in C to F := ",tempconv.ctof(c))
elif choice==2:
	f=eval(input("Enter Temprature in f : ",))
	print("Temprature in F to C := ",tempconv.ftoc(f))
else:
	print("Invalid Choice ")

