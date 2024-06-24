#tkinter Library.

from tkinter import *

def add():
	a=int(n1.get())
	b=int(n2.get())
	c=a+b
	res.config(text=str(c))

root=Tk()
root.title("Simple Calculator")
root.geometry("500x400+300+90")
root.resizable(False,False)
lbl1=Label(root,text="Simple Calculator",fg="blue",font=("Arial 20 bold"))
lbl1.place(x=130,y=0)
lbl2=Label(root,text="Enter First Number :",font=("Arial 10 bold"))
lbl2.place(x=20,y=50)
lbl3=Label(root,text="Enter Second Number :",font=("Arial 10 bold"))
lbl3.place(x=20,y=80)
n1=Entry(root,fg="red",font=("Arial 10 "),width="30")
n1.place(x=200,y=50)
n2=Entry(root,fg="red",font=("Arial 10 "),width="30")
n2.place(x=200,y=80)
res=Label(root,fg="red",font=("Arial 15 bold"))
res.place(x=215,y=120)
btnadd=Button(root,text="ADDITION",font=("Arial 10 bold"),bg="green",width="20",command=add)
btnadd.place(x=150,y=170)
root.mainloop()