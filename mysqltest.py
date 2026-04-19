import os
import mysql.connector

password=os.getenv("DB_PASSWORD")

#connect to mysql
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password=password
)

cursor=conn.cursor()
print("connected succefully")

cursor.execute("create database if not exists pythondb")
print("database created successfully")

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="pythondb"
)
print("connected with database successfully")
cursor=conn.cursor()



cursor.execute(
    '''
    create table if not exists python(
    id int auto_increment primary key,
    libraryname varchar(100)
   
    )
    '''
    )
print("table created successfully")


# for insertion
sql="insert into python( libraryname)values(%s)"
value=("numpy",)
cursor.execute(sql,value)
conn.commit()
print("data inserted successfully")


#for retriving
cursor.execute("select * from python")
rows=cursor.fetchall()
for row in rows:
    print(row)


#update
sql="update python set libraryname= %s where id=%s "
values=("pandas",1)
cursor.execute(sql,values)
conn.commit()
print("After update :")
cursor.execute("select * from python")
rows=cursor.fetchall()
for row in rows:
    print(row)
print("data updated successfully")


#delete 
sql="delete from python where id = %s"
value=(1,)
cursor.execute(sql,value)
conn.commit()

print("After delete :")
cursor.execute("select * from python")
rows=cursor.fetchall()
for row in rows:
    print(row)
print("deleted succesfully")
conn.close()




