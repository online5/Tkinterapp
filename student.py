from Tkinter import *
import Tkinter as tk
import psycopg2



def search(id):
    con = psycopg2.connect(dbname="postgres", user="postgres", password="moserbaer", host="localhost",port=5432);
    cur = con.cursor()
    query = ''' select * from student where id = %s;'''
    cur.execute(query,(id))
    row = cur.fetchone()
    if(row):
        display_search(row)
    con.commit()
    con.close()


def display_search(row):
    listbox=Listbox(frame, width=20,height=1)
    listbox.grid(row=7,column=3)
    listbox.insert(END,row)

def display_all():
     con = psycopg2.connect(dbname="postgres", user="postgres", password="moserbaer", host="localhost",port=5432);
     cur = con.cursor()
     query = '''select * from student;'''
     cur.execute(query)
     row = cur.fetchall()

     listbox=Listbox(frame, width=20,height=5)
     listbox.grid(row=9,column=1)
     for x in row:
         listbox.insert(END,x)


def get_data(name,age,address):
    con = psycopg2.connect(dbname="postgres", user="postgres", password="moserbaer", host="localhost",port=5432);
    cur = con.cursor()
    query='''INSERT INTO Student(Name,AGE,Address) values(%s,%s,%s);'''
    cur.execute(query,(name,age,address))
    print("ValuesInserted.")
    con.commit()
    con.close()


root = Tk()
canvas = Canvas(root,height=480,width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label = Label(frame,text="Enter Details ")
label.grid(row=0,column=1)

label = Label(frame,text="Name")
label.grid(row=1,column=0)

entry_name = Entry(frame)
entry_name.grid(row=1,column=1)


label = Label(frame,text="Age")
label.grid(row=2,column=0)

entry_age = Entry(frame)
entry_age.grid(row=2,column=1)


label = Label(frame,text="Address")
label.grid(row=3,column=0)

entry_addre = Entry(frame)
entry_addre.grid(row=3,column=1)

button = Button(frame,text="Submit", command=lambda:get_data(entry_name.get(),entry_age.get(),entry_addre.get()))
button.grid(row=4,column=1)

label = Label(frame,text="SearchById")
label.grid(row=6,column=1)

label = Label(frame,text="ID")
label.grid(row=7,column=0)

id_search = Entry(frame)
id_search.grid(row=7,column=1)

button = Button(frame,text="Submit", command=lambda:search(id_search.get()))
button.grid(row=7,column=2)

button = Button(frame,text="DisplayAllRecords", command=lambda:display_all())
button.grid(row=8,column=1)


root.mainloop()
