import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="2003",database="project")
cur=mydb.cursor()
def insert():
    a=str(input("Enter book id"))
    b=str(input("Enter book name"))
    c=str(input("Enter Author name"))
    d=str(input("Enter publisher name"))
    e=str(input("Enter genre of book"))
    s="insert into library(Book_id,Book_name,Author_name,publisher_name,Genre_of_book) values('{}','{}','{}','{}','{}')".format(a,b,c,d,e)
    cur.execute(s)
    mydb.commit()


def update():
    a=input("Enter book_id for which update is required")
    b=input("Enter the field name you want to update")
    c=input("Enter value you want to give to that field")
    s=("update library set {}='{}' where book_id='{}'").format(b,c,a)
    cur.execute(s)
    mydb.commit()
    
def selectall():
    cur.execute("select*from library")
    data=cur.fetchall()
    print("The records are as following")
    tup=("Book_id","Book_name","Author_name","Publisher name","Genre","Status","Name of issuing person","Issue date","Due date")
    x=0
    y=1
    for row in data:
        l1=list(row)
        for i in tup:
            print(i,end=':')
            for j in range(x,y):
                print(l1[j])
                x=x+1
                y=y+1
        x=0
        y=1
        print('''


                ''')
    print("End of records")   
def selectauthor():
    ch=str(input("Enter author name"))
    print('''The records are as following
                ''')
    s=("Select*from library where Author_name='{}'").format(ch)
    cur.execute(s)
    data=cur.fetchall()
    print("The records are as following")
    tup=("Book_id","Book_name","Author_name","Publisher name","Genre","Status","Name of issuing person","Issue date","Due date")
    x=0
    y=1
    for row in data:
        l1=list(row)
        for i in tup:
            print(i,end=":")
            for j in range(x,y):
                print (l1[j])
                x+=1
                y+=1
        x=0
        y=1
        print('''


                ''')
    print("End of records")

def selectid():
    ch=str(input("Enter book id"))
    print('''The records are as following
                ''')
    s=("Select*from library where book_id='{}'").format(ch)
    cur.execute(s)
    data=cur.fetchall()
    print("The records are as following")
    tup=("Book_id","Book_name","Author_name","Publisher name","Genre","Status","Name of issuing person","Issue date","Due date")
    x=0
    y=1
    for row in data:
        l1=list(row)
        for i in tup:
            print(i,end=":")
            for j in range(x,y):
                print (l1[j])
                x+=1
                y+=1
        x=0
        y=1
        print('''


                ''')
    print("End of records")
def selectpublisher():
    ch=str(input("Enter publisher name"))
    print('''The records are as following
                ''')
    s=("Select*from library where publisher_name='{}'").format(ch)
    cur.execute(s)
    data=cur.fetchall()
    print("The records are as following")
    tup=("Book_id","Book_name","Author_name","Publisher name","Genre","Status","Name of issuing person","Issue date","Due date")
    x=0
    y=1
    for row in data:
        l1=list(row)
        for i in tup:
            print(i,end=":")
            for j in range(x,y):
                print (l1[j])
                x+=1
                y+=1
        x=0
        y=1
        print('''


                ''')
        
    print("End of records")
def selectname():
    ch=str(input("Enter book name"))
    print('''The records are as following
                ''')
    s=("Select*from library where book_name='{}'").format(ch)
    cur.execute(s)
    data=cur.fetchall()
    print("The records are as following")
    tup=("Book_id","Book_name","Author_name","Publisher name","Genre","Status","Name of issuing person","Issue date","Due date")
    x=0
    y=1
    for row in data:
        l1=list(row)
        for i in tup:
            print(i,end=":")
            for j in range(x,y):
                print (l1[j])
                x+=1
                y+=1
        x=0
        y=1
        print('''


                ''')
    print("End of records")
def status():
    ch=input("Enter Book id")
    s=("Select status,due_date from library where book_id='{}'").format(ch)
    cur.execute(s)
    data=cur.fetchall()
    for row in data:
        if "issued" in row:
            print("Book is already issued")
            print("Due date is",row[1])
        else:
            print("Book is unissued")
            


def delete():
    ch=input("Enter the Book id whose record is to be deleted")
    s=("Delete from Library where book_id='{}'").format(ch)
    cur.execute(s)
    mydb.commit()

def issue():
    from datetime import date
    from datetime import timedelta
    a=input("Enter Book ID you want to issue")
    b=input("Enter your Name")
    today=date.today()
    due=today+timedelta(days=7)
    s=("Update library set status='issued',Name_of_issuing_person='{}',issue_date='{}',due_date='{}' where Book_id='{}'").format(b,today,due,a) 
    cur.execute(s)
    mydb.commit()

def structure():
    print("The structure is as follows")
    cur.execute("desc library")
    tup=('Field','Type','Null','Key','Default','Extra')
    data=cur.fetchall()
    for row in data:
        l1=list(row)
        x=0
        y=1
        for i in tup:
            print(i,end=':')
            for j in range(x,y):
                print(l1[j])
                x+=1
                y+=1
        print()
def unissue():
    a=input("Enter the Book ID to be returned")
    s=("update library set status='Unissued',Name_of_issuing_person=null,Issue_date=null,due_date=null where book_id='{}'").format(a)
    cur.execute(s)
    mydb.commit()

            
def alter():
    print("Press 1 to add a column")
    print("press 2 to modify a column")
    print("press 3 to delete a column")
    a=int(input("Enter your choice"))
    if a==1:
        b=input("Enter column Name")
        c=input("Enter data type")
        s=("alter table library add column {} {}").format(b,c)
        cur.execute(s)
        mydb.commit()
    if a==2:
        b=input("Enter Column name")
        c=input("Enter Data type")
        s=("alter table library modify column {} {}").format(b,c)
        cur.execute(s)
        mydb.commit()
    if a==3:
        b=input("Enter column name")
        s=("Alter table library drop column {}").format(b)
        cur.execute(s)
        mydb.commit()





