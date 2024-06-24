class employee:
	def setValue(self,empid,empname,empsalary):
		self.empid=empid
		self.empname=empname
		self.empsalary=empsalary
	def display(self):
		print("Employee Id = ",self.empid)
		print("Employee Name = ",self.empname)
		print("employee Salary = ",self.empsalary)
e=employee()
eid=int(input("Enter Employee Id : "))
ename=input("Enter Employee Name : ")
esalary=eval(input("Enter Employee salry : "))
e.setValue(eid,ename,esalary)
e.display()