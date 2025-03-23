from tkinter import*
import pandas as pd


win=Tk()

win.title("Address Book")
var1=StringVar()
var2=StringVar()
var3=StringVar()

li=Listbox(win, height=20, width=45, border=3)

but1=Label(win, text="Name:")
but2=Label(win, text="Phone No.")
but3=Label(win, text="Address:")
l1=Label(win, text="Email-id:")

e1=Entry(win, textvariable=var1)
e2=Entry(win, textvariable=var2)
e3=Text(win, width=40, height=10)
e4=Entry(win, textvariable=var3)


datas=[]

def value():
     global datas
     datas.append([var1.get(),var2.get(),var3.get(), e3.get(1.0,"end-1c")])
     store()
     
     
     
def dele1():
     del datas[(li.curselection()[0])]
     store()
     
def view():
     var1.set(datas[(li.curselection()[0])][0])
     var2.set(datas[(li.curselection()[0])][1])
     var3.set(datas[(li.curselection()[0])][2])
     e3.delete(1.0,"end-1c")
     v3=(datas[(li.curselection()[0])][3])
     e3.insert(1.0, v3)
def reset():
     var1.set('')
     var2.set('')
     var3.set('')
     e3.delete(1.0, "end-1c")
          

def store():
     li.delete(0, END)
     for n,l,a,p in datas:
          li.insert(END, n,l)
          
     e1.delete(0,END)
     e2.delete(0, END)
     e3.delete(1.0, "end-1c")
     e4.delete(0, END)


def add():
     df=pd.DataFrame(datas)
     f2=pd.read_excel("C:\\Users\\BHARATHI\\OneDrive\\Desktop\\CODSOFT\\-CODSOFT\\Book1.xlsx")
     df2=pd.DataFrame(f2)
     cd=(df2,df)
     con=pd.concat(cd, axis=0,ignore_index=True)
     fd=pd.DataFrame(con)
     save=fd.to_excel( "C:\\Users\\BHARATHI\\OneDrive\\Desktop\\CODSOFT\\-CODSOFT\\Book1.xlsx", index=False)


   
but4=Button(win, text="Add",command=value, width=10)
but5=Button(win, text="view", command=view, width=10)
but6=Button(win, text="Delete",command=dele1,width=10)
but7=Button(win, text="Reset",command=reset, width=10)
but8=Button(win, text="Upload", command=add)


but1.grid(row=1, columnspan=1)
e1.grid(row=1, column=2)
but2.grid(row=2, columnspan=1)
e2.grid(row=2, column=2)
but3.grid(row=4, columnspan=1)
l1.grid(row=3, columnspan=1)
e3.grid(row=4, column=2)
e4.grid(row=3, column=2)



but4.grid(row=5, column=1)
but5.grid(row=5, column=2)
but6.grid(row=5, column=3)
but7.grid(row=5, columnspan=4)
but8.grid(rowspan=9, column=2)

li.grid(row=8, column=1)


win.mainloop()
