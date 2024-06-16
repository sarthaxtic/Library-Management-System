import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="project")
cur=mydb.cursor()
s="create table Library(Book_id varchar(100),Book_name varchar(200),Author_name varchar(200),publisher_name varchar(200),Genre_of_book varchar(200),status varchar(200),name_of_issuing_person varchar(300),issue_date date,due_date date)"
cur.execute(s)
mydb.commit()
