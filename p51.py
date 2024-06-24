# multiple Inheritance .
from time import sleep
class papa:
	def m1(self):
		sleep(1)
		print("mai m1 hu papa se ")
class mummy:
	def m2(self):
		sleep(1)
		print("mai m2 hu mummy se ")
class child(papa,mummy):
	def m3(self):
		sleep(1)	
		print("mai m3 mummy and papa se ")
c=child()
c.m3()
c.m2()
c.m1()