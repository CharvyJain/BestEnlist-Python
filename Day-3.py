#importing library
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

window = tkinter.Tk()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('300x300')
#Declaring Window Color
window.configure(background="pink")
#below four fields are declared
Firstname = Label(window, text="First Name", bg = "pink", fg="black").grid(row=0, column=0)
LastName = Label(window, text="Last Name", bg = "pink").grid(row=1, column=0)
Email = Label(window, text="Email Id", bg = "pink").grid(row=2, column=0)
Gender = Label(window, text="Choose", bg = "pink").grid(row=3, column=0)
Lang = Label(window, text="Enter Your preferred Language",bg = "pink").grid(row=4, column=0)
Address = Label(window, text="Enter Your Address",bg = "pink").grid(row=5, column=0)
Country = Label(window, text="Enter Your Country Name",bg = "pink").grid(row=6, column=0)
Mobile = Label(window, text="Contact Number",bg = "pink").grid(row=7, column=0)
Github = Label(window, text="Enter Your Github UserName",bg = "pink").grid(row=8, column=0)
Linkedin = Label(window, text="Enter Your LinkedIN Profile",bg = "pink").grid(row=9, column=0)
ttk.Checkbutton(window, text = "I agree to all Terms & Conditions",bg = "pink").grid(row = 10, columnspan = 2)

Firstname1 = Entry(window).grid(row=0, column=1)
Lastname1 = Entry(window).grid(row=1, column=1)
Email1 = Entry(window).grid(row=2, column=1)
var = IntVar()
ttk.Radiobutton(window, text="Male", variable=var, value=1).grid(row = 3, column = 1)
ttk.Radiobutton(window, text="Female", variable=var, value=2).grid(row = 3, column = 2)
Lang1 = Entry(window).grid(row=4, column=1)
addr = Entry(window,height=50).grid(row = 5, column = 1)
Country1 = Entry(window).grid(row=6, column=1)
Phone = Entry(window).grid(row=7, column=1)
Git = Entry(window).grid(row=8, column=1)
link = Entry(window).grid(row=9, column=1)

def hello():
    tkinter.messagebox.showinfo("Confirm", "Your Registration Has Been Successful.")
    
B1 = Button(window, text = "Submit",bd = '5',command = hello).grid(row=11, columnspan = 2)
B1.pack()

window.mainloop()
