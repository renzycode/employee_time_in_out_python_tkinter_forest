import tkinter as tk
from tkinter import ttk
import pymysql
import datetime
from tkinter import messagebox

def getTimeNow(variant):
    if variant=='hms':
        time=datetime.datetime.now().strftime("%I:%M:%S %p")
    else:
        time=datetime.datetime.now().strftime("%I:%M %p")
    return time

print(getTimeNow('hm'))

def connection():
    try: 
        conn=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='time_in_out_system'
        )
        return conn
    except Exception as e:
        print('error: '+e)
        exit()

conn=connection()
cursor=conn.cursor()

def refreshTable():
    for data in treeview.get_children():
        treeview.delete(data)
    for array in read():
        treeview.insert('',tk.END,values=array[1:],iid=array[0])
        print(array)
    treeview.pack()

def read():
    cursor.connection.ping()
    sql="SELECT `id`,`e_id`,`name`,`time_in`,`time_out` FROM time_in_out ORDER BY `id` DESC"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def save(variant,e_id,password,time):
    cursor.connection.ping()
    sql=f"SELECT * FROM employee WHERE e_id='{e_id}' AND password='{password}'"
    cursor.execute(sql)
    result=cursor.fetchone()
    conn.commit()
    conn.close()
    if not result:
        messagebox.showwarning("","Wrong employee id or password")
        return False
    name=result[2]
    cursor.connection.ping()
    sql=f"SELECT * FROM time_in_out WHERE e_id='{e_id}'"
    cursor.execute(sql)
    result=cursor.fetchone()
    conn.commit()
    conn.close()
    if variant=='Time-In':
        if result:
            if result[4]=='----':
                messagebox.showwarning("","You're already in")
                return True
        try:
            cursor.connection.ping()
            sql=f"INSERT INTO time_in_out (`e_id`,`name`,`time_in`,`time_out`) values ('{e_id}','{name}','{time}','----')"
            cursor.execute(sql)
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showwarning("","Error while time in :"+e)
        refreshTable()
    else:
        if result:
            if result[4]!='----':
                messagebox.showwarning("","You're already out")
                return True
        try:
            cursor.connection.ping()
            sql=f"UPDATE time_in_out SET `time_out`='{time}' WHERE `e_id`='{e_id}'"
            cursor.execute(sql)
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showwarning("","Error while time out :"+e)
        refreshTable()
    return True

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

def renderModal(variant):
    modal=tk.Tk()
    modal.title(f"{variant} Modal")
    style=ttk.Style(modal)
    modal.tk.call("source","forest-light.tcl")
    modal.tk.call("source","forest-dark.tcl")
    style.theme_use("forest-dark")
    modal.resizable(False,False)

    modalFrame=ttk.Frame(modal)
    modalFrame.pack()

    modalWidgetsFrame=ttk.LabelFrame(modalFrame,text=variant)
    modalWidgetsFrame.grid(row=0,column=0,padx=20,pady=20)

    e_idEntry=ttk.Entry(modalWidgetsFrame)
    e_idEntry.insert(0,"E-ID")
    e_idEntry.bind("<FocusIn>",lambda e: e_idEntry.delete('0','end'))
    e_idEntry.grid(row=0,column=0,padx=10,pady=[10,5],sticky="ew")

    passwordEntry=ttk.Entry(modalWidgetsFrame)
    passwordEntry.insert(0,"Password")
    passwordEntry.bind("<FocusIn>",lambda e: passwordEntry.delete('0','end'))
    passwordEntry.grid(row=1,column=0,padx=10,pady=[0,5],sticky="ew")

    timeEntry=ttk.Entry(modalWidgetsFrame)
    timeEntry.insert(0,getTimeNow('hm'))
    timeEntry.grid(row=2,column=0,padx=10,pady=[0,5],sticky="ew")
    timeEntry.config(state="disabled")

    submitBtn=ttk.Button(modalWidgetsFrame,text='Submit',command=lambda: submit(modal,variant,str(e_idEntry.get()),str(passwordEntry.get()),str(timeEntry.get())))
    submitBtn.grid(row=4,column=0,padx=10,pady=[0,5],sticky="nsew")

def submit(modal,variant,e_id,password,time):
    print(e_id,password,time)
    if not(e_id and e_id.strip()) or not(password and password.strip()) or e_id=='E-ID' or password=='Password':
        messagebox.showwarning("","Please fill up all entries")
        return
    if save(variant,e_id,password,time):
        modal.destroy()

buttonTimeIn=ttk.Button(widgets_frame,text="Time In",command=lambda: renderModal("Time-In"))
buttonTimeIn.grid(row=0,column=0,padx=10,pady=[10,5],sticky="nsew")

buttonTimeOut=ttk.Button(widgets_frame,text="Time Out",command=lambda: renderModal("Time-Out"))
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

refreshTable()
treeScroll.config(command=treeview.yview)

def updateClock():
    realTimeClock.config(text=getTimeNow('hms'))
    realTimeClock.after(1000,updateClock)

realTimeClock=ttk.Label(text=getTimeNow('hms'),font=('Arial BOLD',20))
realTimeClock.pack(pady=[0,20])
realTimeClock.after(1000,updateClock)

root.mainloop()