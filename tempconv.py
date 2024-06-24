'''
Write a python program to create a module named tempconv. 
In tempconv module create two function ctof() and ftoc(). 
ctof() function converts temperature from centigrade to 
Fahrenheit  and ftoc() function converts temperature from 
Fahrenheit to centigrade. Now import tempconv module 
and test ctof() and ftoc() functions.
'''

def ctof(c):
	resultInF=((c*9/5)+32)
	return resultInF
def ftoc(f):
	resultInC=((f-32)*5/9)
	return resultInC