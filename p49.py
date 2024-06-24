#Multilevel Inheritance.

class A:
	def m1(self):
		print("Hello This is m1 from class A")
class B(A):
	def m2(self):
		print("Hello this is m2 from class B")
class C(B):
	def m3(self):
		print("Hello this is m3 from class C")
c=C()
c.m1()
c.m2()
c.m3()