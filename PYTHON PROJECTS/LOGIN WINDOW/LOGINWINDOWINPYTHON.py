from tkinter import *
from tkinter import messagebox
from forgetpage import forget




t=Tk()
t.title("LOG IN")
#photo = PhotoImage(file =r"C:\user.png")
#t.iconphoto(True,photo)

t.geometry("600x400")

name_var=StringVar()
passw_var=StringVar()

    

def submit():
    
    name=name_var.get()
    password=passw_var.get()
    
    print("The name is : " + name)
    print("The password is : " + password)
    messagebox.showinfo("login", "successfully login")
    
    name_var.set("")
    passw_var.set("")



name_label = Label(t, text = 'User name')
name_label.grid(row=0,column=0)
passw_label = Label(t, text = 'Password')
passw_label.grid(row=1,column=0)

name_entry = Entry(t,textvariable = name_var)
name_entry.grid(row=0,column=1)
passw_entry=Entry(t, textvariable = passw_var, show = '*')
passw_entry.grid(row=1,column=1)

sub_btn=Button(t,text = 'LOGIN', command = submit)
sub_btn.grid(row=2,column=1)
sub_btn=Button(t,text = 'FORGET PASSWORD', command = forget)
sub_btn.grid(row=4,column=1)


t.mainloop()
