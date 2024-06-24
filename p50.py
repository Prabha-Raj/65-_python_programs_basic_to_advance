#Multiple Inheritance.
from time import sleep
class A:
	def m1(self):
		sleep(1)
		print("this is m1 from Class A") 
class B:
	def m2(self):
		sleep(1)
		print("This is m2 From Class B")
class C():
	def m3(self):
		sleep(1)
		print("This is m3 from Class C")
class D(A,B,C):
	def m4(self):
		sleep(1)	
		print("this is m4 from Class D")
d=D()
d.m1()
d.m2()
d.m3()
d.m4()
	