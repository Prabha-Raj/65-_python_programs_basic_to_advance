name=input("Enteer Your Name : ")
print(name)
sname=name.split(" ")
print("Your Sort Name : ",end="")
for n in range(len(sname)-1):
	print(sname[n][0]+".",end="")
print(sname[len(sname)-1])
