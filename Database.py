import psycopg2


def create():
    con = psycopg2.connect(dbname="postgres", user="postgres", password="moserbaer", host="localhost",port=5432);
    cur = con.cursor()
    cur.execute('''
    create table Student(ID serial,Name text,AGE int ,Address text);
    ''')
    print("TableCreated")
    con.commit()
    con.close()


def insert(name,age,address):
    con = psycopg2.connect(dbname="postgres", user="postgres", password="moserbaer", host="localhost",port=5432);
    cur = con.cursor()
    query='''INSERT INTO Student(Name,AGE,Address) values(%s,%s,%s);'''
    cur.execute(query,(name,age,address))
    print("ValuesInserted.")
    con.commit()
    con.close()


if (__name__ == "__main__"):
    name=raw_input("Enter Name.")
    age=input("Enter Age")
    address=raw_input("Enter Address");
    insert(name,age,address)
