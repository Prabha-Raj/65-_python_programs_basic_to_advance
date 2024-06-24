#WAP to calculate Electricity bill.
 
units=int(input("Enter Electricity Unites : "))
if units<1:
	print("Invalid Units")
elif units>=1 and units<=150:
	bill = units*2.40
elif units>150 and units<=300:
	bill = (150*2.40)+(units-150)*3.00
elif units>300:
	bill = (150*2.40)+(150*3.00)+(units-300)*3.20
	
print("Your Total Electricity Bill : ",bill)