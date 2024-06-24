#WAP Temprature Calculator.

choice=int(input("Enter 1 for c to f And 2 fo f to c: "))
 
if choice==1:
	tempInC = eval(input("Enter Temprature in c : "))
	tempInF=((9*tempInC)/5+32)
	print("Temprature In F : ",tempInF)
elif choice==2:
	tempInF=eval(input("Enter Temprature in F : "))
	tempInC=(tempInF-32)*5/9
	print("Temprature In C : ",tempInC)
else:
	print("Invalid Choice !")