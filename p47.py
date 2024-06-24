class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def rectAngle(self):
		return (self.l*self.b)
	def rectPeri(self):
		return 2*(self.l+self.b)
l=int(input("Enter Length of Rectangle : "))
b=int(input("Enter Breadth of Rectangle : "))
obj=Rectangle(l,b)
print("Area if Rectangle : ",obj.rectAngle())
print("Primeter of Rectangle : ",obj.rectPeri())



