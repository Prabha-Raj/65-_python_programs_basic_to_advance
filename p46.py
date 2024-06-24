#usef defined constructor;

class Test:
	def __init__(self):
		print("Constructor Execution 1....")
	def m1(self):
		print("Method Execution 2.....")
t1=Test()
t2=Test()
t3=Test()
t1.m1()