import sqlite3


#connect to database
conn=sqlite3.connect("mydatabase.db")
print("Connected Successfully")

# #bridge to connect 
cursor=conn.cursor()

# cursor.execute("drop table users ")
# print("table deleted successfully")

#create table
cursor.execute(
    '''
create table if not exists users(
id integer primary key,
name text,
age integer
)
'''
)
print("table created successfully")


#insert data
cursor.execute(
    "insert into users(name,age)values(?,?)",("pratiksha",24))
cursor.executemany(
    "insert into users(name,age)values(?,?)",
    [
        ("nikita",89),
        ("pari",67)
    ]
)


#fetch data
cursor.execute("select * from users ")
rows=cursor.fetchall()

print("data in table:")
for row in rows:
    print(row)



#update data
cursor.execute("update users set age=? where name=?",(21,"nikita"))
print("updated ")

cursor.execute("select * from users ")
rows=cursor.fetchall()
print("data in table:")
for row in rows:
    print(row)



#Delete data
cursor.execute("delete from users where name=?",("nikita",))
print("deleted successfully")

cursor.execute("select * from users ")
rows=cursor.fetchall()
print("data in table:")
for row in rows:
    print(row)
conn.commit()
conn.close()









