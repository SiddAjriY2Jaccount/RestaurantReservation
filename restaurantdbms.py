import pymysql
from tkinter import *
conn = pymysql.connect(host='localhost', port=3306, user='sidd', passwd='123', db='reservations')
#cur = conn.cursor()


class Login:
    def __init__(self, f1):
        self.f1=f1;
        self.Uname=StringVar()
        self.Password=StringVar()
        self.Email = StringVar()

        self.label_0 = Label(f1, text="Login",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        self.label_1 = Label(f1, text="Username",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(f1, textvar=self.Uname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(f1, text="Password",width=20,font=("bold", 10))
        self.label_2.place(x=79,y=180)

        self.entry_2 = Entry(f1, textvar=self.Password)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(f1, text="Email",width=20,font=("bold", 10))
        self.label_3.place(x=90,y=230)

        self.entry_3 = Entry(f1, textvar=self.Email)
        self.entry_3.place(x=240,y=230)

        self.btn = Button(f1, text='Submit',width=20,bg='dark blue',fg='white', command=self.insertlogin)
        self.btn.place(x=180,y=300)

    def insertlogin(self):
        name=self.Uname.get()
        email=self.Email.get()
        password=self.Password.get()
           #conn = pymysql.connect(host='localhost', port=3306, user='sidd', passwd='123', db='reservations')
        cur = conn.cursor()
           #cur.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
        sql1 = "INSERT INTO `users` (`username`,`password`,`email`) VALUES (%s, %s, %s)"
        cur.execute(sql1, (name, password, email))
        conn.commit()
        cur.close()
        self.f1.destroy()
        #global root
        f2 = Frame(root,width=500,height=500)
        f2.pack()
        global Username
        Username = self.Uname
        Lab = Label(f2, text=Username.get())
        Lab.pack()


root = Tk()
root.geometry('500x500')
root.title("Login")
f1 = Frame(root,width=500,height=500)
f1.pack()
login = Login(f1)
root.mainloop()
