#E Bill

unit = int(input("Enter Units : "))
if unit>=1 and unit<=150:
	bill=unit*2.40
elif unit>150 and unit<=300:
	bill=(150*2.40)+(unit-150)*3.00
else
	bill=(150*2.40)+(150*3.00)+(unit-300)*3.20
print("Your Total Electricity Bill : ",bill)