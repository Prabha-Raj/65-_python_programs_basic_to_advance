# super():- When Method overloding .

class parent(object):
	def altered(self):
		print("parent altered")
class child(parent):
	def altered(self):
		print("child before parent altered")
		super(child,self).altered()
		print("child after parent altered")
dad=parent()
son=child()
son.altered()