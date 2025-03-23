from tkinter import*

win=Tk()

win.geometry("700x600")
win.title("To-Do List")
var1=StringVar()

def add():
    v1=t1.get()
    aad=li1.insert(END,v1)
    t1.delete(0,END)
def add1():
     selected=li1.curselection()
     li2.insert(END,li1.get(selected))
     li1.delete(END)
     
def dele1():
    selected_checkboxs=li2.curselection()
    for selected_checkbox in selected_checkboxs[::-1]:
        li2.delete(selected_checkbox)        
    

def dele():
    selected_checkboxs=li1.curselection()
    for selected_checkbox in selected_checkboxs[::-1]:
        li1.delete(selected_checkbox)

    


l1=Label(win, text="Add Task")
t1=Entry(win, width=50, textvariable=var1)

l2=Label(win, text="Task To Do")
l3=Label(win, text="Finished Task")
li1=Listbox(win, height=20, width=35)
li2=Listbox(win, height=20, width=35)
b1=Button(win, text="Add",command=add)
b2=Button(win, text="Delete Added Task", command=dele)
b3=Button(win, text="Task Finished", command=add1)
b4=Button(win, text="Delete Finished Task", command=dele1)



l1.grid(row=1, column=2)
l2.grid(row=2, column=2)
l3.grid(row=2, column=4)
t1.grid(row=1, column=3)
li1.grid(row=2, column=3)
li2.grid(row=2, column=5)
b1.grid(row=5, column=2)
b2.grid(row=5, column=3)
b3.grid(row=5, column=4)
b4.grid(row=5, column=5)

win.mainloop()
