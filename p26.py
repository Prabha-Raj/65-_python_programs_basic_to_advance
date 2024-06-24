#static list.
friends=["Prabha", "Abhay", "Shailendra Kumar", "Sourabh"]
print("Before sorting Your list is :  ",friends)
friends.sort
print("After sorting your list is :  ",friends)

#Dynamic list
mylist=[]
element=int(input("How Many Number Are Want to in list : "))
print("Enter ",element," Elements for List : ")
for i in range(element):
	n=eval(input())
	mylist.append(n)
print(mylist)
#for finding maximum Number
print("Maximum number in your list ",max(mylist))
print("Minimun number in your list  ",min(mylist))
	