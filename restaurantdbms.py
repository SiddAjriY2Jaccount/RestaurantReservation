import pymysql
from tkinter import *
import tkinter.messagebox
conn = pymysql.connect(host='localhost', port=3306, user='sidd', passwd='123', db='reservations')
#cur = conn.cursor()



class Login:
    def __init__(self, f):
        self.f=f
        self.Uname=StringVar()
        self.Password=StringVar()
        self.Email = StringVar()

        self.label_0 = Label(f, text="Register yourself here",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        self.label_1 = Label(f, text="Username",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(f, textvar=self.Uname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(f, text="Password",width=20,font=("bold", 10))
        self.label_2.place(x=79,y=180)

        self.entry_2 = Entry(f, textvar=self.Password)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(f, text="Email",width=20,font=("bold", 10))
        self.label_3.place(x=90,y=230)

        self.entry_3 = Entry(f, textvar=self.Email)
        self.entry_3.place(x=240,y=230)

        self.btn = Button(f, text='Submit',width=20,bg='dark blue',fg='white', anchor="center", command=self.insertlogin)
        self.btn.place(x=180,y=300)

    def insertlogin(self):
        name=self.Uname.get()
        email=self.Email.get()
        password=self.Password.get()
        global Username
        Username = self.Uname
        print(Username.get())
        #to check if primary key aready EXISTS
        cur1 = conn.cursor()
        sql1 ="SELECT username FROM users"
        cur1.execute(sql1)
        result1 = cur1.fetchall()
        for row in result1:
            un = row[0]
            if(un==Username.get()):
                tkinter.messagebox.showinfo("PrimaryKeyError", "Username has already been taken")
        cur1.close()
        #if not, then enter user details into user table
        cur = conn.cursor()
        #cur.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
        sql = "INSERT INTO users (username,password,email) VALUES (%s, %s, %s)"
        cur.execute(sql, (name, password, email))
        conn.commit()
        cur.close()

        self.f.destroy()
        #global root#self.f1.title("RESTAURANT DETAILS AND CUISINE")
        f1 = Frame(root,width=1000,height=1000)
        f1.pack()
        #Lab = Label(f2, text=Username.get())
        #Lab.pack()
        page1 = Page1(f1)


class Page1:
    def __init__(self, f1):
        self.f1 = f1
        self.f1.pack()

        global Username
        print(Username.get())

        self.label1 = Label(self.f1, text=" All you need to know - Affiliated Restaurants ", font = ("bold",15))
        self.label1.pack(side=TOP)

        cur = conn.cursor()
        sql = "SELECT * from restaurant_details"
        cur.execute(sql)
        result = cur.fetchall()

        self.label2 = Label(self.f1, text="Restaurant Details")
        #self.label2.place(x=70, y=50, anchor="w")
        self.label2.pack(side=TOP)

        for row in result:
            rid = row[0]
            rid = (str)(rid)
            name = row[1]
            locality = row[2]
            valet = row[3]
            toprint = ("RID " + rid + " - " + name + " - " + "Location : " + locality + " - " + "Valet : "+ valet)
            self.label4 = Label(self.f1, text=toprint)
            self.label4.pack(side = TOP)

        self.btn1 = Button(self.f1, text='Next',width=20,bg='red',fg='white', anchor="center", command=self.nextpage)
        self.btn1.pack(side=BOTTOM)

        #self.btn2 = Button(self.f1, text='Previous',width=20,bg='red',fg='white', anchor="center", command=self.prevpage)
        #self.btn2.pack(side=BOTTOM)

        cur.close()

    def nextpage(self):
        self.f1.destroy()
        f2 = Frame(root,width=1000,height=1000)
        f2.pack()
        page2 = Page2(f2)


class Page2:
    def __init__(self, f2):
        self.f2 = f2
        self.f2.pack()
        global Username
        print(Username.get())
        self.label1 = Label(self.f2, text=" Menu ", font = ("bold",15))
        self.label1.pack(side=TOP)

        cur = conn.cursor()
        sql = "SELECT * from cuisine"
        cur.execute(sql)
        result = cur.fetchall()

        self.label2 = Label(self.f2, text="Cuisine on offer")
        #self.label2.place(x=70, y=50, anchor="w")
        self.label2.pack(side=TOP)

        for row in result:
            rid = row[0]
            rid = (str)(rid)
            itemname = row[1]
            calories = (str)(row[2])
            type =row[3]
            price = (str)(row[4])
            serves = row[5]
            toprint = ("RID " + rid + " - " + itemname + " - " + "Calories : " + calories + " - " + type + " - " + price +"$ - " + serves)
            self.label4 = Label(self.f2, text=toprint)
            self.label4.pack(side = TOP)

        self.btn1 = Button(self.f2, text='Next',width=20,bg='red',fg='white', anchor="center", command=self.nextpage)
        self.btn1.pack(side=BOTTOM)

        self.btn2 = Button(self.f2, text='Previous',width=20,bg='red',fg='white', anchor="center", command=self.prevpage)
        self.btn2.pack(side=BOTTOM)

        cur.close()

    def nextpage(self):
        self.f2.destroy()
        f3 = Frame(root,width=700,height=500)
        f3.pack()
        page3 = Page3(f3)

    def prevpage(self):
        self.f2.destroy()
        f1 = Frame(root,width=1000,height=1000)
        f1.pack()
        page11 = Page1(f1)

class Page3:
    def __init__(self, f3):
        self.f3 = f3
        self.Rid= IntVar()
        self.Seats=IntVar()
        self.Uname = StringVar()
        global Username
        print(Username.get())
        self.Uname = Username

        self.labela = Label(self.f3, text=" BOOKING OF TABLES ", width = 20, font = ("bold",20))
        self.labela.place(x=180, y=13)
        self.label_0 = Label(self.f3, text="Reserve seats here, " + self.Uname.get(),width=30,font=("bold", 10))
        self.label_0.place(x=210,y=83)

        self.label_1 = Label(self.f3, text="RID",width=20,font=("bold", 10))
        self.label_1.place(x=110,y=130)

        self.entry_1 = Entry(self.f3, textvar=self.Rid)
        self.entry_1.place(x=270,y=130)

        self.label_2 = Label(self.f3, text="No. of Seats",width=20,font=("bold", 10))
        self.label_2.place(x=110,y=180)

        self.entry_2 = Entry(self.f3, textvar=self.Seats)
        self.entry_2.place(x=270,y=180)

        self.btn = Button(self.f3, text='Submit',width=20,bg='dark blue',fg='white', anchor="center", command=self.insertbookings)
        self.btn.place(x=250,y=300)

        self.btn1 = Button(self.f3, text='Previous',width=20,bg='red',fg='white', anchor="center", command=self.prevpage)
        self.btn1.place(x=250, y=400)

    def prevpage(self):
        self.f3.destroy()
        f2 = Frame(root,width=1000,height=1000)
        f2.pack()
        page21 = Page2(f2)

    def insertbookings(self):
        global Username
        print(Username.get())
        name=Username.get()
        rid=self.Rid.get()
        seats=self.Seats.get()
        global RID
        RID = self.Rid
        #if not, then enter details into Bookings table
        cur = conn.cursor()
        #cur.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
        sql = "INSERT INTO bookings (rid, username, no_of_seats) VALUES (%s, %s, %s)"
        cur.execute(sql, (rid, name, seats))
        conn.commit()
        cur.close()

        print(RID.get())

        stringrid = (str)(rid)
        print(stringrid)
        stringseats = (str)(self.Seats.get())
        print(stringseats)
        toprint1 = name + " has booked " + stringseats + " seats for RID " + stringrid
        tkinter.messagebox.showinfo("Notice", toprint1)

        self.f3.destroy()
        #global root#self.f1.title("RESTAURANT DETAILS AND CUISINE")
        f4 = Frame(root,width=1000,height=1000)
        f4.pack()
        #Lab = Label(f2, text=Username.get())
        #Lab.pack()
        page4 = RatingPage(f4)

class RatingPage:
    def __init__(self, f4):
        self.f4=f4
        self.Stars=IntVar()
        global Username
        self.myName = Username.get()
        global RID
        self.myRID = RID.get()

        self.label_0 = Label(self.f4, text="Please rate your experience, "+ self.myName +" for RID : "+(str)(self.myRID),width=40,font=("bold", 10))
        self.label_0.place(x=170,y=53)

        self.label_1 = Label(self.f4, text="On a scale of 1-10 :",width=20,font=("bold", 10))
        self.label_1.place(x=165,y=130)

        self.entry_1 = Entry(self.f4, textvar=self.Stars)
        self.entry_1.place(x=320,y=130)

        self.btn = Button(self.f4, text='Submit',width=20,bg='dark blue',fg='white', anchor="center", command=self.insertrating)
        self.btn.place(x=250,y=300)

    def insertrating(self):
        stars=self.Stars.get()
        name=self.myName
        rid=self.myRID

        #if not, then enter user details into user table
        cur = conn.cursor()
        #cur.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
        sql = "INSERT INTO restaurant_rating (rid, username, stars) VALUES (%s, %s, %s)"
        cur.execute(sql, ((int)(rid), name, (int)(stars)))
        conn.commit()
        cur.close()

        self.f4.destroy()
        #global root#self.f1.title("RESTAURANT DETAILS AND CUISINE")
        f5 = Frame(root,width=1000,height=1000)
        f5.pack()
        #Lab = Label(f2, text=Username.get())
        #Lab.pack()
        thankspage = Thankspage(f5)


class Thankspage:
    def __init__(self, f5):
        self.f5=f5
        self.label_0 = Label(self.f5, text="THANK YOU",width=20,font=("bold", 30))
        self.label_0.pack(side="top", fill="both", expand=True)


root = Tk()
root.geometry('700x500')
root.title("RESTAURANT RESERVATIONS DESKTOP APPLICATION")
f = Frame(root,width=500,height=500)
f.pack()
login = Login(f)
root.mainloop()
