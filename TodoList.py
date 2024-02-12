from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        li_b.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning !!!", "Please enter some/any task.")

def deleteTask():
    li_b.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('YOUR TO-DO LIST:')
ws.config(bg='#2ADADF')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=15)

li_b = Listbox(
    frame,
    width=30,
    height=10,
    font=("Times",18 , "bold"),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
li_b.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
   li_b.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

li_b.config(yscrollcommand=sb.set)
sb.config(command=li_b.yview)

my_entry = Entry(
    ws,
    font=('times', 20)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

AddT_B = Button(
    button_frame,
    text='Add New Task',
    font=('Helvetica 12 bold italic'),
    bg='#c5f776',
    padx=15,
    pady=10,
    command=newTask
)
AddT_B.pack(fill=BOTH, expand=True, side=LEFT)

DelT_B = Button(
    button_frame,
    text='Delete Any Task',
    font=('Helvetica 12 bold italic'),
    bg='#ff8b61',
    padx=15,
    pady=10,
    command=deleteTask
)
DelT_B.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()
            
