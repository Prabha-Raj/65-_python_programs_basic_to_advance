#Inheritance

class Bulldog:
	def grawl(self):
		print("Bruno...")
		print("Gur...,Gur...")
class Rundog(Bulldog):
	def bark(self):
		print("sheru...")
		print("Bho...,Bho..")
dog=Rundog()
dog.bark()
dog.grawl()