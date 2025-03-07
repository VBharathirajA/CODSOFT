import tkinter as tk

win=tk.Tk()

win.geometry("600x600")
win.title("To-Do List")





l1=tk.Label(win, text="Add Task")
t1=tk.Text(win, width=40, height=10)

l2=tk.Label(win, text="Task List")
li1=tk.Listbox(win, height=20, width=35)


l1.grid(row=1, column=1)
l2.grid(row=1, column=2)
t1.grid(row=2, column=1)
li1.grid(row=2, column=2)
