import pymysql
from tkinter import *
import tkinter.messagebox
conn = pymysql.connect(host='localhost', port=3306, user='sidd', passwd='123', db='reservations')
#cur = conn.cursor()
global Username


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
        Username = self.Uname
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
            toprint = (rid + " - " + name + " - " + "Location : " + locality + " - " + "Valet : "+ valet)
            self.label4 = Label(self.f1, text=toprint)
            self.label4.pack(side = TOP)


            #self.label5 = Label(self.f1, text="LOST")
            #self.label5.place(x=20, y=100)
            #ogy = ogy * 2
            #ogx = ogx + 20



root = Tk()
root.geometry('500x500')
root.title("RESTAURANT RESERVATIONS DESKTOP APPLICATION")
f = Frame(root,width=500,height=500)
f.pack()
login = Login(f)
root.mainloop()
