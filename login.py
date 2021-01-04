import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
from tkinter import messagebox
import random
import tkinter.ttk
from tkinter import ttk
import mysql.connector
from operator import itemgetter
import datetime
from PIL import ImageTk
key=4
ki=-4

db_connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="encdec"
)
cursor1 = db_connection.cursor()
db_connection2=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="encdec"
)
cursor2 = db_connection2.cursor()
print(db_connection)
mainWindow=Tk()
mainWindow.title("Login")
mainWindow.geometry("1366x700+-5+-4")
bg_icon = ImageTk.PhotoImage(file="enc2.jpg",master=mainWindow)
bg_lbl = Label(mainWindow, image=bg_icon).place(x=0, y=-100, relwidth=1)
#title = Label(mainWindow, text="Encryption and Decryption System", font=("Verdana", 30), bg="black",
              #fg="white",
              #bd=10, relief=GROOVE)
#title.place(x=0, y=0, relwidth=1)
l=Label(mainWindow,text="Sign-In",font=("Minecrafter Alt", 35),bg="#01172F",fg="#3FC1FF",bd=0)
l.place(x=580,y=80)
key2 = StringVar()
key2 = "key is: "
def start():
    strt = Tk()
    strt.title("Login")
    strt.geometry("1366x700+-5+-4")
    bg_icon = ImageTk.PhotoImage(file="enc.jpg")
    bg_lbl = Label(strt, image=bg_icon).place(x=0, y=-140, relwidth=1)



def Register():
    regW = Tk()
    regW.title("Create New Account!")
    regW.geometry("1366x700+-5+-4")

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="encdec"
    )

    def exit():
        regW.destroy()

    def insertreg():
        cursor = db_connection.cursor()
        if nam.get()=="" or usert.get()=="" or passt==""  or passt2.get()=="":
            messagebox.showinfo("","please fill all enteries!")
        else:
            insert=("insert into login(name,user,password) values(%s,%s,%s)")
            values=[nam.get(),usert.get(),passt.get()]
            cursor.execute(insert,values)
            if passt.get()== passt2.get():
                db_connection.commit()
                messagebox.showinfo("Done!",nam.get()+" your new account is created!")
                regW.destroy()
            else:
                messagebox.showerror("Oops!", nam.get() + " your Password didnt matched!")

    bg_icon = ImageTk.PhotoImage(file="enc.jpg",master=regW)
    bg_lbl = Label(regW,image=bg_icon, bg="#01172F").place(x=0, y=0, relwidth=1)
    title = Label(regW, text="Create New Account", font=("Minecrafter Alt", 35),bg="#01172F",fg="#3FC1FF",bd=0, relief=GROOVE)
    title.place(x=0,y=80,relwidth=1)
    lble = Label(regW, text="Enter Name",font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0)
    lble.place(x=380, y=200)

    nam = Entry(regW, font=("Techno at Dusk", 20),fg="#01172F",bg="#3FC1FF",bd=0,width=15)
    nam.place(x=700, y=200)
    lble = Label(regW, text="Enter Username", font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0,width=17)
    lble.place(x=350, y=240)
    usert = Entry(regW, font=("Techno at Dusk", 20),fg="#01172F",bg="#3FC1FF",bd=0,width=15)
    usert.place(x=700, y=240)
    lble = Label(regW, text="Enter Password", font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0,width=17)
    lble.place(x=350, y=280)
    passt = Entry(regW, font=("Techno at Dusk", 20),fg="#01172F",bg="#3FC1FF",bd=0,show="*",width=15)
    passt.place(x=700, y=280)
    lble = Label(regW, text="Re-Enter Password", font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0,width=17)
    lble.place(x=370, y=320)
    passt2 = Entry(regW, font=("Techno at Dusk", 20),fg="#01172F",bg="#3FC1FF",bd=0,show="*",width=15)
    passt2.place(x=700, y=320)
    ############################################
    encryptbtn = Button(regW, text="Sign Up",font=("Minecrafter Alt", 20),bg="#001228",fg="#3FC1FF",bd=0,comman=insertreg)
    encryptbtn.place(x=485, y=380)
    encryptbtn = Button(regW, text="Cancel",font=("Minecrafter Alt", 20),bg="#001228",fg="#3FC1FF",bd=0,command=exit)
    encryptbtn.place(x=635, y=380)


def Loginf():
    enc=Tk()
    enc.title("Encryption and Decryption System")
    enc.geometry("1366x700+-5+-4")
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="encdec"
    )
    usernam=t1.get()
    e = StringVar()
    alphabet = " abcdefghijklmnopqrstuvwxyzBC1234567890ADEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=|<>,.?{}:[]\/'"
    newkey = 0
    res = StringVar()
    newmsg = ""
    res = ""
    bg_icon = ImageTk.PhotoImage(file="enc.jpg",master=enc)
    bg_lbl = Label(enc,image=bg_icon, bg="#01172F").place(x=0, y=0, relwidth=1)
    cursor=db_connection.cursor()
    def encrypt():
        rest.delete(first=0, last=100)
        newmsg = ""
        #entkey.insert("1",key)
        if txte.get() == "":
            print("d")
        elif txte.get() != "":
            for character in txte.get():
                position = alphabet.find(character)
                newposition = (position + key) % 89
                newchar = alphabet[newposition]
                newmsg += newchar
            rest.insert("1",newmsg)
    def decrypt():
        rest.delete(first=0, last=100)
        newmsg = ""
        if txte.get() == "":
            print("d")
        elif txte.get() != "":
            for character in txte.get():
                position = alphabet.find(character)
                newposition = (position + ki) % 89
                newchar = alphabet[newposition]
                newmsg += newchar
            rest.insert("1",newmsg)
    def insert():
        cursor = db_connection.cursor()
        now=datetime.datetime.now()
        if txte.get()!="" and rest.get()!="":
            insert=("insert into enctext(text,encrypted,keyno,user,date) values(%s,%s,%s,%s,%s)")
            values=[txte.get(),rest.get(),key,usernam,now.strftime("%d-%m-%y %H:%M:%S")]
            cursor.execute(insert,values)
            db_connection.commit()
            messagebox.showinfo("done","Encrypted data Saved!")
        else:
            messagebox.showinfo("Oops","Encrypt/Decrypt Something first!")
    def insert2():
        cursor = db_connection.cursor()
        now = datetime.datetime.now()
        if txte.get() != "" and rest.get() != "":
            insert=("insert into dectext(text,decrypted,keyno,user,date) values(%s,%s,%s,%s,%s)")
            values=[txte.get(),rest.get(),ki,usernam,now.strftime("%d-%m-%y %H:%M:%S")]
            cursor.execute(insert,values)
            db_connection.commit()
            messagebox.showinfo("done","Decrypted Data Saved!")
        else:
            messagebox.showinfo("Oops","Encrypt/Decrypt Something first!")

    def ckey():
        global ki
        global key
        key = int(entkey.get())
        ki = key - (key * 2)
        messagebox.showinfo("done","new key is "+str(key))

    def clearEntry():
        txte.delete(first=0,last=100)
        rest.delete(first=0,last=100)
    def showdb():
        sdb = Tk()
        sdb.title("Encryption and Decryption System")
        sdb.geometry("1366x700+-5+-4")
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="encdec"
        )
        bg_icon = ImageTk.PhotoImage(file="enc.jpg", master=sdb)
        bg_lbl = Label(sdb, image=bg_icon, bg="#01172F").place(x=0, y=0, relwidth=1)
        def showdata():
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="encdec"
            )
            global key2
            cur=db_connection.cursor()
            insert = ("Select * from enctext where user= %s")
            values = [usernam]
            cur.execute(insert,values)
            result=cur.fetchall()
            if len(result)!=0:
                enctable.delete(*enctable.get_children())
                for row in result:
                    enctable.insert('',END,values=row)
            db_connection.commit()

            #########################

            insert = ("Select * from dectext where user= %s")
            values = [usernam]
            cur.execute(insert,values)
            result=cur.fetchall()
            if len(result)!=0:
                dectable.delete(*dectable.get_children())
                for row in result:
                    dectable.insert('',END,values=row)
            db_connection.commit()
            db_connection.close()
        ########################################################
        def selectrow(ev):
            global key2
            txt.delete(first=0, last=100)
            encdec.delete(first=0, last=100)
            keydisp.delete(first=0, last=100)
            viewI=enctable.focus()
            learnd=enctable.item(viewI)
            row=learnd['values']
            if row[1]!="":
                txt.insert("0",row[1])
                encdec.insert("0",row[2])
                keydisp.insert("0","key is "+str(row[3]))
        def selectrow2(ev):
            txt.delete(first=0, last=100)
            encdec.delete(first=0, last=100)
            keydisp.delete(first=0, last=100)
            viewI=dectable.focus()
            learnd=dectable.item(viewI)
            row=learnd['values']
            txt.insert("0",row[1])
            encdec.insert("0",row[2])
            keydisp.insert("0","key is "+str(row[3]))

        #scroll_y=Scrollbar(sdb,orient =HORIZONTAL)
        enctable=ttk.Treeview(sdb, height=12, columns=("S.no", "Text", "Encrypted","Key","Date","User"))
        #scroll_y.pack(side=RIGHT,fill =Y)
        enctable.heading("S.no",text="S.no")
        enctable.heading("Text",text="Text")
        enctable.heading("Encrypted",text="Encrypted")
        enctable.heading("Key", text="Key")
        enctable.heading("Date",text="Date")
        enctable.heading("User",text="User")
        ####################################################
        enctable['show']='headings'

        enctable.column("S.no",width=70)
        enctable.column("S.no",width=100)
        enctable.column("S.no",width=100)
        enctable.column("S.no",width=100,)
        enctable.column("S.no",width=70)
        enctable.column("S.no",width=100)
        enctable.bind("<ButtonRelease-1>",selectrow)
        enctable.place(x=10, y=65)
        ######################################################################################
        dectable=ttk.Treeview(sdb, height=12, columns=("S.no", "Text", "Decrypted","Key","Date","User"))
        #scroll_y.pack(side=RIGHT,fill =Y)
        dectable.heading("S.no",text="S.no",)
        dectable.heading("Text",text="Text")
        dectable.heading("Decrypted",text="Decrypted")
        dectable.heading("Key",anchor=CENTER, text="Key")
        dectable.heading("Date",text="Date")
        dectable.heading("User",text="User")
        ####################################################
        dectable['show']='headings'

        dectable.column("S.no",width=70)
        dectable.column("S.no",width=100)
        dectable.column("S.no",width=100)
        dectable.column("S.no",width=100,anchor=CENTER)
        dectable.column("S.no",width=70)
        dectable.column("S.no",width=100)

        dectable.bind("<ButtonRelease-1>", selectrow2)
        dectable.place(x=10, y=410)

        lbl=Label(sdb,text="Encrypted Data Details",bd=10, relief=GROOVE,font=("Minecrafter Alt", 25),bg="#01172F",fg="#3FC1FF")
        lbl2=Label(sdb,text="Decrypted Data Details",bd=10, relief=GROOVE,font=("Minecrafter Alt", 25),bg="#01172F",fg="#3FC1FF")
        lbl.place(x=0,y=0,relwidth=1)
        lbl2.place(x=0,y=350,relwidth=1)
        showdata()
        lblkey = Label(sdb, text="Text", font=("calibri", 14),bg="#01172F",fg="#3FC1FF",bd=0)
        lblkey.place(x=1120, y=90)
        txt = Entry(sdb, font=("calibri", 18),fg="#01172F",bg="#3FC1FF",bd=0,width=12)
        txt.place(x=1120, y=120)
        lblkey = Label(sdb, text="Encypted/Decrypted", font=("calibri", 13),bg="#01172F",fg="#3FC1FF",bd=0)
        lblkey.place(x=1120, y=160)
        encdec = Entry(sdb, font=("calibri", 18),fg="#01172F",bg="#3FC1FF",bd=0,width=12)
        encdec.place(x=1120, y=190)
        keydisp = Entry(sdb,  font=("calibri", 18),fg="#01172F",bg="#3FC1FF",bd=0,width=12)
        keydisp.place(x=1120, y=230)

#################################################################################
    title = Label(enc, text="Data Encryption and Decryption System", font=("Minecrafter Alt", 33),bg="#01172F",fg="#3FC1FF",
                  bd=10, relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)
    lblkey = Label(enc, text="Welcome "+usernam ,font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0)
    lblkey.place(x=40,y=75)
    kbt = Button(enc, text="My Database",font=("Minecrafter Alt", 20),bg="#000407",fg="#3FC1FF",bd=0,command=showdb)
    kbt.place(x=1000, y=75)
    entkey = Entry(enc, text=str(key), font="Calibri 20",fg="#01172F",bg="#3FC1FF",bd=0,width=14)
    entkey.place(x=1003, y=120)
    kbt = Button(enc, text="Change Key", font=("Minecrafter Alt", 20),bg="#000407",fg="#3FC1FF",bd=0,command=ckey)
    kbt.place(x=1003, y=165)
    lble = Label(enc, text="Enter Text to Encrypt/Decrypt:",font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0)
    lble.place(x=370,y=170)
    txte = Entry(enc,font=("Calibri", 20),fg="#01172F",bg="#3FC1FF",bd=0,width=36)
    txte.place(x=370,y=220)

    ####3


    encryptbtn = Button(enc, text="Encrypt",font=("Minecrafter Alt", 20),bg="#000407",fg="#3FC1FF",bd=0,command=encrypt)
    encryptbtn.place(x=395,y=285)
    encryptbtn = Button(enc, text="Decrypt", font=("Minecrafter Alt", 20),bg="#000407",fg="#3FC1FF",bd=0,command=decrypt)
    encryptbtn.place(x=395, y=335)
    encryptbtn = Button(enc, text="Save Encrypted", font=("Minecrafter Alt", 20),bg="#000407",fg="#3FC1FF",bd=0,command = insert)
    encryptbtn.place(x=560, y=285)
    encryptbtn = Button(enc, text="Save Decrypted",font=("Minecrafter Alt", 20),bg="#000407",fg="#3FC1FF",bd=0,command=insert2)
    encryptbtn.place(x=560, y=335)
    encryptbtn = Button(enc, text="Clear",font=("Minecrafter Alt", 22),bg="#000407",fg="#3FC1FF",bd=0,command=clearEntry,width=25)
    encryptbtn.place(x=370, y=460)
    resl = Label(enc, text="Result is:",font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0)
    resl.place(x=370, y=395)
    rest = Entry(enc, font=("Calibri", 20),fg="#01172F",bg="#3FC1FF",bd=0, width=23)
    rest.place(x=550, y=395)


    print("enc")

def Logincheck():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="encdec"
    )

    sel = ("select user from login")
    sel2 = ("select password from login")
    cursor1.execute(sel)
    cursor2.execute(sel2)
    user=t1.get()
    pas=t2.get()
    e=[]
    p=[]
    for i in cursor1:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res=list(map(itemgetter(0),e))
    res2=list(map(itemgetter(0),p))
    k=len(res)
    i=1
    while i<k:
        if res[i]==user and res2[i]==pas:
            Loginf()
            break
        i=i+1
    else:
        messagebox.showinfo("something wrong!","Incorrect Username or Password!")
l1 = Label(mainWindow,text="Password", font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0)
l1.place(x=400,y=220)

t1 = Entry(mainWindow, font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0,width=15)
t1.place(x=610,y=180)
l2 = Label(mainWindow,text="Username", font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0)
l2.place(x=400,y=180)
t2 = Entry(mainWindow,font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0,show="*",width=15)
t2.place(x=610,y=220)

Login = Button(mainWindow,text="Login",font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0, command=Logincheck)
Login.place(x=610,y=270)
Reg = Button(mainWindow,text="Register",font=("Minecrafter Alt", 20),bg="#01172F",fg="#3FC1FF",bd=0, command=Register)
Reg.place(x=730,y=270)

mainWindow.mainloop()