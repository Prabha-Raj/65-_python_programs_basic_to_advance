#Random Number 

import random
lower=int(input("Enter Lower Lemit : "))
upper=int(input("Enter Upper Lemit : "))
no=random.randint(lower,upper)
num=1
while num>0:
	num=int(input("Enter No. "))
	if no>(num+5):
		print("Your No is Too low  !")
	elif no<(num-5):
		print("Your No is Too Heigh !")
	elif no>num:
		print("your No is Near but low ! ")
	elif no<num:
		print("Your No is Near but height !")
	elif no==num:
		print("Congratulation You are The Winner !")
		print("And Computer Genrated No is :=> ",no)
		break

#print(no)