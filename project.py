


#import urllib
##p = urllib.urlopen("http://web2.qatar.cmu.edu/~mkhan2/")
##line = p.readline()
##print line
##
from Tkinter import *
class main():
    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,background='DarkSlateGray1')
        self.frame.pack(fill="both", expand=True)
        self.l2=Label(self.frame,text='io',font="Helvetica 10 ",bg='Grey25',width=10)
        self.l2.grid(row=0,column=0)
        self.opt1= Button(self.frame, text="By Typing",font="Helvetica 10 ",bg="blue",command=self.clickB1,width=10)
        self.opt1.grid(row=1,column=0)#option 1 of searching (by typing)

        self.opt2= Button(self.frame, text="By Scanning",font="Helvetica 10",bg="blue",command=self.clickB1,width=10)
        self.opt2.grid(row=2,column=0)#option 2 of searching (by scanning the barcode)
        self.welc=Label(self.frame,text='Welcome!',font="Courier 40")
        self.welc.pack(fill="both", expand=True)
    def clickB1(self):
        self.opt1.config(activebackground="red")
        B1wnd=Toplevel(wnd)
        b1wnd=option1(B1wnd)
class option1():
    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,bg="light salmon")
        self.frame.pack(fill="both", expand=True)
        self.b1=Button(self.frame,text='o')
        self.b1.pack()
wnd=Tk()
mainwnd=main(wnd)
wnd.title("Check Nutritional Facts")
mainloop()
wnd.destroy()
