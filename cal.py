from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("1280x720")

op1 = Entry(window, width="15")
num1 = Label(window, text="a")
op2 = Entry(window, width="15")
num2 = Label(window, text="b")

num1.grid(column= 0, row = 0)
num2.grid(column= 0, row = 1)
op1.grid(column= 1, row = 0)
op2.grid(column= 1, row = 1)

def add():
    a = op1.get()
    b = op2.get()

    if(a == "" or b == ""):
        messagebox.showerror("Error", "Feilds cannot be left blank")
        return
    try:
        x = int(a)
        y = int(b)
    except:
        messagebox.showerror("Error", "Enter valid number")
        return
    messagebox.showinfo("Sum", a + " + " + b + " = " + str(x + y))

sum = Button(window, command = add, text = "+")
sum.grid(column = 0, row = 2)

def sub():
    a = op1.get()
    b = op2.get()

    if(a == "" or b == ""):
        messagebox.showerror("Error", "Feilds cannot be left blank")
        return
    try:
        x = int(a)
        y = int(b)
    except:
        messagebox.showerror("Error", "Enter valid number")
        return
    messagebox.showinfo("Sum", a + " - " + b + " = " + str(x - y))

dif = Button(window, command = sub, text = "-")
dif.grid(column = 0, row = 3)

def mul():
    a = op1.get()
    b = op2.get()

    if(a == "" or b == ""):
        messagebox.showerror("Error", "Feilds cannot be left blank")
        return
    try:
        x = int(a)
        y = int(b)
    except:
        messagebox.showerror("Error", "Enter valid number")
        return
    messagebox.showinfo("Sum", a + " x " + b + " = " + str(x * y))

prod = Button(window, command = mul, text = "X")
prod.grid(column = 0, row = 4)

def div():
    a = op1.get()
    b = op2.get()

    if(a == "" or b == ""):
        messagebox.showerror("Error", "Feilds cannot be left blank")
        return
    try:
        x = int(a)
        y = int(b)
    except:
        messagebox.showerror("Error", "Enter valid number")
        return
    messagebox.showinfo("Sum", a + " / " + b + " = " + str(x / y))

quot = Button(window, command = div, text = "/")
quot.grid(column = 0, row = 5)

window.mainloop()
