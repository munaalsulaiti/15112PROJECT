#    15-112: Principles of Programming and Computer Science
#    HW06 Programming: Implementing a Chat Client
#    Name      : Muna Al-Sulaiti
#    AndrewID  : masulait
#    File Created: 7/11 
#    Modification History:
#    Start            End
#    7/11  4:30pm     7/11  6:30pm
#    9/11  5:00pm     9/11  7:00pm
#    10/11 4:00pm     10/11 6:00pm
#    11/11 3:00pm     11/11 7:00pm


import urllib#for later refrence

itemNbarcode={'9501100014283':'Qarmoosh Chips','2000000335032':'Rayan Water','032894010339':'California Gradens Backed beans','780863185778':'sample','6294003532987':'KitKat'}
from Tkinter import *
#from masulaithw3 import * #for later refrence

#item=decodeBarcode('barcode2.jpg')#this only temporary
#print itemNbarcode[item],'h'
class main():
    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,bg='light cyan')
        self.frame.pack(fill="both", expand=True)
        self.l1=Label(self.frame,text='Welcome !',bg='light cyan',width=10,font="Courier 40")
        self.l1.grid(row=0)
        self.l2=Label(self.frame,text='look up',bg='light cyan',width=10,font="Courier 25")
        self.l2.grid(row=1,column=0,columnspan=3)
        self.l3=Label(self.frame,text='an item',bg='light cyan',width=10,font="Courier 25")
        self.l3.grid(row=2,column=0,columnspan=3)
        self.opt1= Button(self.frame, text="By Typing",width=10,bg="DarkSlateGray1",command=self.clickB1)
        self.opt1.grid(row=1,column=2)#option 1 of searching (by typing)
        self.opt2= Button(self.frame, text="By Scanning",width=10,bg="DarkSlateGray1",command=self.clickB2)
        self.opt2.grid(row=2,column=2)#option 2 of searching (by scanning the barcode)
##        self.wel=Label(self.frame,text='Welcome!')
##        self.wel.pack()
    def clickB1(self):#searching by typing
        self.opt1.config(activebackground="red")
        B1wnd=Toplevel(wnd)
        b1wnd=option1(B1wnd)
    def clickB2(self):#searching by scanning
        self.opt2.config(activebackground="red")
        B2wnd=Toplevel(wnd)
        b2wnd=option2(B2wnd)
class option1():
    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,bg="bisque")
        self.frame.pack(fill="both", expand=True)
        self.b1=Button(self.frame,text='search',command=self.lookup,bg='light salmon')#after clicking we search
        self.b1.grid(row=1,column=2)
        self.itemname=Entry(self.frame)#the item to look up
        self.itemname.grid(row=1,column=1)
    def lookup(self):
        item=self.itemname.get()
        self.itemname.delete(0,END)#empty the entry box after clicking for search
        #need to read the url for the item and find the ingredients list and the facts
class option2():
    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,bg="bisque")
        self.frame.pack(fill="both", expand=True)
        self.b1=Button(self.frame,text='search',command=self.lookup,bg='light salmon')#after clicking we search
        self.b1.grid(row=1,column=2)
        #just temporarly we are looking at the pictures and not the captures
        #self.item=itemNbarcode[item]
    def lookuponline(self):
        #here we'll lookup the item's name and info online
        pass
    def displaProd(self):
        pass
wnd=Tk()
mainwnd=main(wnd)
wnd.title("Check Nutritional Facts")
mainloop()
#wnd.destroy() #gives an error if added
