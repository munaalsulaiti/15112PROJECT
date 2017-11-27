#    15-112: Principles of Programming and Computer Science
#    HW06 Programming: Implementing a Chat Client
#    Name      : Muna Al-Sulaiti
#    AndrewID  : masulait
#    File Created: 7/11 

from PIL import Image, ImageTk
#from cv import * this doesn't neither does it with cv3 
from urllib import * #for later refrence
import re
itemNbarcode={'032894010339':'California Gradens Backed beans','780863185778':'sample','6294003532987':'KitKat'}
from Tkinter import *
##if __name__ =='__main__':
##    capture=CaptureFromCAM(0)
##    Namedwindow('image')
##    while True:
##        frame=QueryFrame(capture)
##        ShowImage('image',frame)
##        k=WaitKey(10)
##        if k % 256 ==27:
##            break
##    Destroywindow('image')
#from masulaithw3 import * #for later refrence
##
##link='https://www.nutritionvalue.org/search.php?food_query='+item+'&page='

nutrition=re.compile('<tbody>(.*)</tbody>')#the part were the ingredients are

##facts=re.compile("http://www.myfitnesspal.com/food/calories/cup-of-joe-coffee-[0-9]+")
##
##if 'Chacolate' or "coco" in facts:
##    print 'false'
###item=decodeBarcode('barcode2.jpg')#this only temporary
##print itemNbarcode[item],'h'
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
        self.opt1= Button(self.frame, text="By Typing",width=15,bg="DarkSlateGray1",command=self.clickB1)
        self.opt1.grid(row=1,column=2)#option 1 of searching (by typing)
        self.opt2= Button(self.frame, text="By Scanning",width=15,bg="DarkSlateGray1",command=self.clickB2)
        self.opt2.grid(row=2,column=2)#option 2 of searching (by scanning the barcode)
        self.check= Button(self.frame, text="check an ingrediant",width=15,bg="DarkSlateGray1",command=self.Check)
        self.check.grid(row=3,column=2)
        self.help=Button(self.frame,text='Help?',width=10,bg="DarkSlateGray1",command=self.clickB3)
        self.help.grid(row=4,column=0)
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
    def clickB3(self):#for help
        self.help.config(activebackground="red")
        B3wnd=Toplevel(wnd)
        b3wnd=option3(B3wnd)
    def Check(self):#check for an ingiediant
        self.check.config(activebackground="red")
        cwnd=Toplevel(wnd)
        Cwnd=checkfor(cwnd)
class checkfor():
    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,bg="bisque")
        self.frame.pack(fill="both", expand=True)
        self.b1=Button(self.frame,text='search',bg='light salmon')#after clicking we search
        self.b1.grid(row=1,column=2)
        self.itemname=Entry(self.frame)#the item to look up
        self.itemname.grid(row=1,column=1)
        
class option1():
    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,bg="bisque")
        self.frame.pack(fill="both", expand=True)
        self.b1=Button(self.frame,text='search',command=self.lookup,bg='light salmon')#after clicking we search
        self.b1.grid(row=1,column=2)
        self.itemname=Entry(self.frame)#the item to look up
        self.itemname.grid(row=1,column=1)
        self.b2=Button(self.frame,text='search',command=self.lookupq,bg='light salmon')#after clicking we search
        self.b2.grid(row=2,column=2)
        self.qitemname=Entry(self.frame)#the item to look up
        self.qitemname.grid(row=2,column=1)
    def lookupq(self):
        qitem=self.qitemname.get()
        qitem=qitem.split()
        print qitem
        self.qitemname.delete(0,END)
        f=open('products.txt')
        g=f.readline()
        g=g.split()
        print len(g)
        l=[]
        while g:
            g=f.readline()
            g=g.split()
            print g
            if qitem in g:
                pic=g[-1]
                print pic
                image = Image.open(pic)
                photo = ImageTk.PhotoImage(image)

    def lookup(self):
        item=self.itemname.get()
        self.itemname.delete(0,END)#empty the entry box after clicking for search
        #need to read the url for the item and find the ingredients list and the facts
        #we need re and urllib to look it up
        n=1
        link='https://www.nutritionvalue.org/search.php?food_query='+str(item)+'&page=1'
        page=urlopen(link)

            #link='https://www.nutritionvalue.org/search.php?food_query=+item+&page=[\d]+
        title=re.compile("title='(.*)'>")
        print 'pp['
        li=re.compile("<a href='^[href]+'></a>")
        findtitle=re.findall(title,page)
        findli=re.findall(li,page)
        l=[]
        l[:]=range(2,16)
        for i in l:
           print findtitle[i]
           print findli[i]
           print '\n'
class option2():

    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,bg="bisque")
        self.frame.pack(fill="both", expand=True)
        self.b1=Button(self.frame,text='search',command=self.lookup,bg='light salmon')#after clicking we search
        self.b1.grid(row=1,column=2)
        self.infoFound=True
        #just temporarly we are looking at the pictures and not the captures
        #self.item=itemNbarcode[item]
    
    def lookuponline(self):
        #here we'll lookup the item's name and info online
        #if the product wasn't found:
            #set self.infoFound=False
        if self.infoFound==True:
            infownd=Toplevel(wnd)
            Infownd=INFO(infownd)
            
                    
        pass
    def displaProd(self):
        pass
class option3():
    def __init__(self,parent=None):
        self.parent=parent
        self.frame=Frame(self.parent,bg="bisque")
        self.frame.pack(fill="both", expand=True)
        self.show=Text(self.frame)
        self.show.pack()
        self.show.insert(END,'There are two options for searching')#the help info
        self.show.config(state=DISABLED)
        self.b1=Button(self.frame,text='got it',command=self.goback,bg='light salmon')#after clicking we search
        self.b1.pack()
    
    def goback(self):
        self.parent.destroy()
class INFO():#this class is for info displaying
    def __init__(self,parent=None):#
        self.frame=Frame(self.parent,bg="bisque")
        self.frame.pack()
        self.info='web info as a lst'
        self.chart=Listbox(self.frame)
        self.chart.pack()
        self.chart.insert
        for value in self.info:
            self.chart.insert(END, value)
##        for valu
#find the info
#if product was recognised display else show message
#display the info in a chart
#find and display the picture
#either database or online
#use opencv and fill the rectangle with the barcode
wnd=Tk()
mainwnd=main(wnd)
wnd.title("Check Nutritional Facts")
mainloop()
#wnd.destroy() #gives an error if added
