#WAP tamprature converter by using user input

def converter(c,f):
	temp1=(f-32)*5/9
	temp2=((c*9)/5)+32
	return [temp1,temp2]
t1=eval(input("Enter Tempreture in C : "))
t2=eval(input("Enter Temprature in F : "))
print("Temprature in f to c : ",converter(t1,t2)[0])
print("Temprature in c to f : ",converter(t1,t2)[1])