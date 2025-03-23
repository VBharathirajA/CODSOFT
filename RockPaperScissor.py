from tkinter import *
import random

win=Tk()

win.title("Rock Paper Scissor")
win.geometry("300x300")

l1=Label(win, text="Rock Paper Scissor Game")

def rock():
     uchoice="rock"
     choice(uchoice)

def paper():
    uchoice="paper"
    choice(uchoice)

def scissor():
    uchoice="scissor"
    choice(uchoice)
    


def choice(choice1):
    t1.delete(0,END)
    e2.delete(0,END)
    choices=["rock","paper", "Scissors"]
    fchoice=random.choice(choices)
    t1.insert(END, fchoice)
    if choice1 == fchoice:
        e2.insert(END, "Match tie!")
    elif((choice1=="rock" and choices=="scissors")or
         (choice1=="paper" and choices=="rock")or
         (choice1=="scissors" and choices=="paper")):
        e2.insert(END, "Wow, You win!")
    else:
        e2.insert(END, "Computer win!")
    
        

l2=Label(win, text="Choose one")
t1=Entry(win)
e2=Entry(win)
but1=Button(win, text="Rock",command=rock)
but2=Button(win, text="Paper",command=paper)
but3=Button(win, text="Scissor",command=scissor)



l1.pack(fill=BOTH, expand=True)
l2.pack(fill=BOTH, expand=True)
but1.pack(fill=BOTH, expand=True)
but2.pack(fill=BOTH, expand=True)
but3.pack(fill=BOTH, expand=True)

t1.pack(fill=BOTH, expand=True)
e2.pack(fill=BOTH, expand=True)


win.mainloop()
