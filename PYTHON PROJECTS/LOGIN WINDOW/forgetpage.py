from tkinter import *
from tkinter import messagebox
from functools import partial

def forget():
    
   
    t=Tk()
    t.title("RESET PASSWORD WINDOW")

    t.geometry("600x400")
    
    name_var1=StringVar()
    passw_var1=StringVar()
    passw_var2=StringVar()
  
    def submit1(passw_var1,passw_var2,name_var1):
        
        #name1=name_var1.get()
        #password1=passw_var1.get()
        #password2=passw_var2.get()
        
        if passw_var1.get() == passw_var2.get(): 
            print("entered User name :" + name_var1.get())
            print("new password is :" + passw_var2.get())

        #if password1== password2: 
        #   print("entered User name :" + name1)
        #   print("entered password :" + password1)
        #   print("reentered password :" + password2)
            messagebox.showinfo("password reset successfully","YOUR PASSWORD CHANGED!")
            
            name_var1.set("")
            passw_var1.set("")
            passw_var2.set("")
            
        else :
            messagebox.askretrycancel("reset failed", "PASSWORD NOT MATCHED!")
            
            passw_var2.set("")
           
          
            
    name_label = Label(t, text = 'User name')
    name_label.grid(row=0,column=0)
    name_entry = Entry(t,textvariable = name_var1)
    name_entry.grid(row=0,column=1)
      
    passw_label = Label(t, text = 'new password')
    passw_label.grid(row=1,column=0)
    name_entry = Entry(t,textvariable = passw_var1)
    name_entry.grid(row=1,column=1)
    
    passw_label = Label(t, text = 'confirm password')
    passw_label.grid(row=2,column=0)
    passw_entry2=Entry(t, textvariable = passw_var2, show = '*')
    passw_entry2.grid(row=2,column=1)
    
    submit_btn_command = partial(submit1,passw_var1,passw_var2,name_var1)

    reset_btn=Button(t,text = 'RESET PASSWORD', command = submit_btn_command)
    reset_btn.grid(row=3,column=1)

    mainloop()
    
#forget()
    
