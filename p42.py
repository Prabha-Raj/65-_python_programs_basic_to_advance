class demo:
	def test(self):
		print("Hello World")
	def sum(self,a,b):
		return (a+b)
	def sub(self,a,b):
		return (a-b)
	def mul(self,a,b):
		return (a*b)
	def div(self,a,b):
		return (a/b)
	def rem(self,a,b):
		return (a%b)
	def prime(self,a):
		count=0
		for i in range(1,a+1):
			if a%1==0:
				count+=1
		if count==2:
			return "Is Prime No"
		else:
			return "Is Non Prime No"
				

d=demo()
d.test()
demo().test()
a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
print("Summation = ",d.sum(a,b))
print("Subtraction = ",d.sub(a,b))
print("Multiplication = ",d.mul(a,b))
print("Division = ",d.div(a,b))
print("Remender = ",d.rem(a,b))
print(d.prime(a))





