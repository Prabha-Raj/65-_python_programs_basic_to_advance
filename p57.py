
string=input("Enter String :")
print(string)
rs="".join(reversed(string))
print(rs)
if rs==string:
	print("This string is Palindrom Number ")
else:
	print("This string is Not Palindrom Number")