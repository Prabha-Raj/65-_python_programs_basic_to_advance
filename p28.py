#sum of Dynamic list Elements


mylist=[]
print("Enter 5 Number : ")
sum=0
for i in range(5):
	element=int(input())
	mylist.append(element)
	sum=sum+element
print(mylist)
print(sum)