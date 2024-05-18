from tkinter import * 
from tkinter.messagebox import showinfo

class L:
    def __init__(self,master):
        Label(master,text="CUZINHO HJ?").pack()
        faco = Button(master,text="SIM",command= lambda:self.sim(master))
        faco.pack(side="left")
        nao = Button(master,text="TENHO MEDO.",command= lambda:self.nem(master))
        nao.pack(side="right")
    def nem(event,master):
        master.destroy()
        root = Tk()
        L(root)
        root.mainloop()
    def sim(event,master):
        showinfo(message="SE PREPARA \n         ")
        master.destroy()

root = Tk()
L(root)
root.mainloop()