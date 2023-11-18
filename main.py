import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import messagebox

def getTimeNow(variant):
    if variant=='hms':
        time=datetime.datetime.now().strftime("%I:%M:%S %p")
    else:
        time=datetime.datetime.now().strftime("%I:%M %p")
    return time

print(getTimeNow('hm'))

root=tk.Tk()
root.title("Employee Time-In-Out System")
style=ttk.Style(root)
root.tk.call("source","forest-light.tcl")
root.tk.call("source","forest-dark.tcl")
style.theme_use("forest-dark")
root.geometry("580x400")
root.resizable(False,False)

frame=ttk.Frame(root)
frame.pack()

widgets_frame=ttk.LabelFrame(frame,text="Manage")
widgets_frame.grid(row=0,column=0,padx=[10,5],pady=10,sticky="n")

buttonTimeIn=ttk.Button(widgets_frame,text="Time In")
buttonTimeIn.grid(row=0,column=0,padx=10,pady=[10,5],sticky="nsew")

buttonTimeOut=ttk.Button(widgets_frame,text="Time Out")
buttonTimeOut.grid(row=1,column=0,padx=10,pady=[0,5],sticky="nsew")

buttonExcel=ttk.Button(widgets_frame,text="Download Excel")
buttonExcel.grid(row=2,column=0,padx=10,pady=[0,5],sticky="nsew")

buttonClear=ttk.Button(widgets_frame,text="Clear Data")
buttonClear.grid(row=3,column=0,padx=10,pady=[0,5],sticky="nsew")

treeFrame=ttk.Frame(frame)
treeFrame.grid(row=0,column=1,padx=[5,10],pady=10,sticky="n",ipadx=5,ipady=5)

treeScroll=ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right",fill="y")

cols=("E-ID","Name","Time In","Time Out")
treeview=ttk.Treeview(treeFrame,show="headings",yscrollcommand=treeScroll.set,columns=cols,height=13)
treeview.heading("E-ID",text="E-ID",anchor="w")
treeview.heading("Name",text="Name",anchor="w")
treeview.heading("Time In",text="Time In",anchor="w")
treeview.heading("Time Out",text="Time Out",anchor="w")
treeview.column("E-ID",width=50)
treeview.column("Name",width=110)
treeview.column("Time In",width=70)
treeview.column("Time Out",width=70)

myArray=[
    [1,'e-1234','carlo','8:20 AM','6:00 PM'],
    [2,'e-1245','shaun','8:01 AM','5:40 PM'],
    [3,'e-2257','miguel','7:20 AM','6:30 PM'],
    [4,'e-7741','joseph','7:54 AM','5:22 PM']
]

for data in treeview.get_children():
    treeview.delete(data)
for array in myArray:
    treeview.insert('',tk.END,values=array[1:],iid=array[0])
    print(array)

treeview.pack()
treeScroll.config(command=treeview.yview)

def updateClock():
    realTimeClock.config(text=getTimeNow('hms'))
    realTimeClock.after(1000,updateClock)

realTimeClock=ttk.Label(text=getTimeNow('hms'),font=('Arial BOLD',20))
realTimeClock.pack(pady=[0,20])
realTimeClock.after(1000,updateClock)

root.mainloop(]