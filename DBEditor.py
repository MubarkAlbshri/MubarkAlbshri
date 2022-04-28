#هذي النسخه الوحيدة بدون اعطال أو مشاكل
from sqlite3 import *

db = connect("C:/Users/ehm-7/Desktop/intro.db")
cr = db.cursor()
cr.execute(
    "create table if not exists Users (name TEXT, age INTEGER, user_id INTEGER)"
)

enter = input("Add, Edit, Get or Delete? answer with A, E, G, D: ").capitalize()

#Add
if enter == "Add" or enter == "A":
    userenter = int(input("Enter How Many: "))
    for i in range(userenter):
        cr.execute("select user_id from Users")
        records = cr.fetchall()
        # print()
        userenter = [len(records) + 1,input("Enter User Name: "),int(input("Enter User Age: "))]
        cr.execute(f"insert into Users(user_id, name, age) values({userenter[0]}, '{userenter[1].capitalize()}', {userenter[2]})")





#Edit
elif enter == "Edit" or enter == "E":

    userenter = input("Edit Name, Id Or Age? Answer With N, I, A: ").capitalize()
    if userenter == "N" or userenter == "Name":
        Id = input("Enter The Id: ")
        newName = input("Enter New Name: ")
        cr.execute(f"update Users set name ='{newName.capitalize()}' where user_id = {int(Id)}")
    elif userenter == "A" or userenter == "Age":
        Id = input("Enter The Id: ")
        newAge = input("Enter New Age: ")
        cr.execute(f"update Users set age ='{newAge}' where user_id = {int(Id)}")
    elif userenter == "I" or userenter == "Id":
        name = input("Enter Name: ")
        newId = int(input("Enter New Id: "))
        cr.execute(f"update Users set user_id ='{newId}' where name = '{name.capitalize()}'")






#Get
elif enter == "Get" or enter == "G" :
    userenter = input("All, User id Or Last id? Answer With A, Ui, Li: ").capitalize()
    if userenter == "All" or userenter == "A":
        cr.execute("select user_id, name from Users")
        records = cr.fetchall()
        for row in records:
            print(f"UserId => {row[0]}, UserName => {row[1]}")
    elif userenter == "User id" or userenter == "Ui":
        userenter = int(input("Enter User Id: "))
        cr.execute(f"select user_id, name, age from Users where user_id = {userenter}")
        records = cr.fetchall()
        for row in records:
            print(f"UserId => {row[0]}, UserName => {row[1]}, UserAge => {row[2]}")
    elif userenter == "Last id" or userenter == "Li":
        cr.execute("select user_id from Users")
        records = cr.fetchall()
        print("Id = ", records[len(records) - 1])





#Delete
elif enter == "Delete" or enter == "D":
    userenter = input("All Or With User Id? Answer With A, U: ").capitalize()
    if userenter == "A" or userenter == "All":
        cr.execute("delete from Users")
    elif userenter == "U" or userenter == "User id":
        userenter = input("Enter User Id: ")
        cr.execute(f"delete from Users where user_id = {int(userenter)}")

db.commit()
db.close()
