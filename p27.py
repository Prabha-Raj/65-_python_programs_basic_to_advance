#Dynamic list 
 
flist=[]
element=int(input("How many Number are you want store in your list : "))
print("Enter ",element," Elements for list : ")
for i in range(element):
	e=input()
	flist.append(e)
print("Before sorting ",flist)
flist.sort()
print("After sorting in Acsending ",flist)
flist.reverse()
print("After sortin in Decsending Order ",flist)
#print("After reverse ",flist)
