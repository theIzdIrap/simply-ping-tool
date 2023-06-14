#!/usr/bin/python
from tkinter import *
from tkinter import ttk
import os

win = Tk()


#tk settings

win.geometry("600x300")
win.title("Ping Tool")
win.resizable(False,False)


#delete function
def delete():
    label3.destroy()



#get function for get entry and ping

def get_value():
   global label2
   global label3
   global response
   e_text=entry.get()
   response = os.system("ping " + e_text)
   if response == 0:
       label3 = Label(win, text=str(e_text) + " is up", font=('Century 15 bold'))
       label3.pack()
   else:
       label3 = Label(win, text=str(e_text) + " is down", font=('Century 15 bold'))
       label3.pack()


#entry settings

entry = ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)


#button settings

button = ttk.Button(win, text="Enter", command= get_value)
button.pack()
button = ttk.Button(win, text="Delete", command= delete)
button.pack()
win.mainloop()
