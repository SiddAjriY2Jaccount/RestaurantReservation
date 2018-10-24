import pymysql
from tkinter import *
import tkinter.messagebox
conn = pymysql.connect(host='localhost', port=3306, user='sidd', passwd='123', db='reservations')


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       self.f1 = self
       Page.__init__(self, *args, **kwargs)
       #label = Label(self, text="This is page 1")
       #label.pack(side="top", fill="both", expand=True)
       self.label1 = Label(self.f1, text=" All you need to know - Affiliated Restaurants ", font = ("bold",15))
       self.label1.pack(side=TOP)

       cur = conn.cursor()
       sql = "SELECT * from restaurant_details"
       cur.execute(sql)
       result = cur.fetchall()

       self.label2 = Label(self.f1, text="Restaurant Details")
       #self.label2.place(x=70, y=50, anchor="w")
       self.label2.pack(side=TOP)

       #self.label3 = Label(self.f1, text="Menu")
       #self.label3.place(x=350, y=50, anchor="w")
       for row in result:
           self.label4 = Label(self.f1, text=row)
           self.label4.pack(side = TOP)
       cur.close()


class Page2(Page):
   def __init__(self, *args, **kwargs):
       self.f1=self
       Page.__init__(self, *args, **kwargs)
       #label = Label(self, text="This is page 2")
       #label.pack(side="top", fill="both", expand=True)
       self.label1 = Label(self.f1, text=" Cuisine ", font = ("bold",15))
       self.label1.pack(side=TOP)

       cur = conn.cursor()
       sql = "SELECT * from cuisine"
       cur.execute(sql)
       result = cur.fetchall()

       self.label2 = Label(self.f1, text="RID - Itemname - Calorie Count - Type of food - Price - Serves")
       #self.label2.place(x=70, y=50, anchor="w")
       self.label2.pack(side=TOP)

       #self.label3 = Label(self.f1, text="Menu")
       #self.label3.place(x=350, y=50, anchor="w")
       for row in result:
           rid = row[0]
           itemname = row[1]
           calories = row[2]
           food = row[3]
           price = row[4]
           serves = row[5]
           toprint = ( + " - " + itemname + " - ")
           self.label4 = Label(self.f1, text=row)
           self.label4.pack(side = TOP)
       cur.close()


class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView:
    def __init__(self, f):
        #Frame.__init__(self, *args, **kwargs)
        self.f = f;
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = Button(buttonframe, text="Page 3", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()


root = Tk()
root.geometry("500x500")

mainframe = Frame(root, width=500, height=500)
page2 = MainView(mainframe)
#main.pack(side="top", fill="both", expand=True)
root.mainloop()
