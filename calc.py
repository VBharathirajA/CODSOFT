from tkinter import*

win=Tk()
f1=Frame(win)
f1.grid(rowspan=5, columnspan=1)


win.geometry("800x800")
win.title("Calculator")
photo=PhotoImage(file="C:\\Users\\BHARATHI\\Downloads\\calc.logo.png")
win.iconphoto(False, photo)



e1=Entry(f1, width=43)
e1.focus()
e1.grid(rowspan=1, columnspan=15)

e2=Entry(f1, width=43)
e2.grid(row=1, columnspan=15)
e2.focus()

def b1t(text):
     e1.insert(END,text)
    
def handle_click(text):
     e2.insert(END, text)

def bat():
    value1=int(e1.get())
    value2=int(e2.get())
    add=value1+value2
    e1.delete(0, END)
    e2.delete(0, END)
    e1.insert(END, add)


def bst():
    value1=int(e1.get())
    value2=int(e2.get())
    add=value1-value2
    e1.delete(0, END)
    e2.delete(0, END)
    e1.insert(END, add)

def bmt():
    value1=int(e1.get())
    value2=int(e2.get())
    add=value1*value2
    e1.delete(0, END)
    e2.delete(0, END)
    e1.insert(END, add)

def bdt():
    value1=int(e1.get())
    value2=int(e2.get())
    add=value1/value2
    e1.delete(0, END)
    e2.delete(0, END)
    e1.insert(END, add)


    
def bct():
    e1.delete(0, END)






    
    
frame= lambda: b1t("7") 
b1=Button(f1, text="7" , width=8, command= frame)
b2=Button(f1, text="4",width=8 , command= lambda: [b1t("4"),  handle_click("4")])
b3=Button(f1, text="1",width=8, command= lambda: b1t("1"))
b4=Button(f1, text="8",width=8, command= lambda: b1t("8"))
b5=Button(f1, text="5",width=8, command= lambda: b1t("5"))
b6=Button(f1, text="2",width=8, command= lambda: b1t("2"))
b7=Button(f1, text="0",width=8, command= lambda: b1t("0"))
b8=Button(f1, text="9",width=8, command= lambda: b1t("9"))
b9=Button(f1, text="6",width=8, command= lambda: b1t("6"))
b0=Button(f1, text="3",width=8, command= lambda: b1t("3"))
bc=Button(f1, text="c",width=8, command= bct)
be=Button(f1, text="00",width=8, command= lambda: b1t("00"))
ba=Button(f1, text="+",width=8, command=bat)
bs=Button(f1, text="-",width=8, command=bst)
bm=Button(f1, text="x",width=8, command=bmt)
bd=Button(f1, text="/",width=8, command=bdt)





b1.grid(row=2, column=0)
b2.grid(row=3, column=0)
b3.grid(row=4, column=0)
bc.grid(row=5, column=0)
b4.grid(row=2, column=1)
b5.grid(row=3, column=1)
b6.grid(row=4, column=1)
b7.grid(row=5, column=1)
b8.grid(row=2, column=2)
b9.grid(row=3, column=2)
b0.grid(row=4, column=2)
be.grid(row=5, column=2)
ba.grid(row=2, column=3)
bs.grid(row=3, column=3)
bm.grid(row=4, column=3)
bd.grid(row=5, column=3)





