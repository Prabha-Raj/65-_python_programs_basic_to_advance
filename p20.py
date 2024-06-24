#Simple calculator by Using if Else .
num1=eval(input("Enter First Number: "))
num2=eval(input("Enter Second Number: "))
print("Enter 1 for Summation : ")
print("Enter 2 for Substraction : ")
print("Enter 3 for Division : ")
print("Enter 4 for Multiplecation : ")
print("Enter 5 for Remender : ")
ch=eval(input("Select Operat : "))
if ch==1:
	result=num1+num2
elif ch==2:
	result=num1-num2
elif ch==3:
	result=num1//num2
elif ch==4:
	result=num1*num2
elif ch==5:
	result=num1%num2
else:
	print("Invalid Choice ! ")
print("Your Result is : ",result)