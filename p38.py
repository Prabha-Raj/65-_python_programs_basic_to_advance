#calling of udm module

import prabha
num1=int(input("Enter first Number : "))
num2=int(input("Enter Second Number : "))
sum=prabha.add(num1,num2)
grt=prabha.greatest(num1,num2)
print("Sum = ",sum)
print("Greatest = ",grt)