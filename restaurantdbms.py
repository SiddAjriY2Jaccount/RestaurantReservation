import pymysql
from tkinter import *

root = Tk()

#conn = pymysql.connect(host='localhost', port=3306, user='sidd', passwd='123', db='reservations')
#cur = conn.cursor()
#cur.execute("SELECT * FROM restaurant_details")

#print(cur.description)
#print()


#for row in cur:
    #print(row)
    #label = Label(root, text=row)
    #label.pack()


root.geometry('500x500')
root.title("Login")



Username=StringVar()
Password=StringVar()
Email = StringVar()

def insertlogin():
   name=Username.get()
   email=Email.get()
   password=Password.get()
   conn = pymysql.connect(host='localhost', port=3306, user='sidd', passwd='123', db='reservations')
   cur = conn.cursor()
   #cur.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   sql1 = "INSERT INTO `users` (`username`,`password`,`email`) VALUES (%s, %s, %s)"
   cur.execute(sql1, (name, password, email))
   conn.commit()


label_0 = Label(root, text="Login",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Username",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root, textvar=Username)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root, textvar=Password)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Email",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root, textvar=Email)
entry_3.place(x=240,y=230)

Button(root, text='Submit',width=20,bg='dark blue',fg='white', command=insertlogin).place(x=180,y=300)


root.mainloop()

cur.close()
conn.close()

root.mainloop()
