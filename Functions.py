import mysql.connector as SQLC
from tkinter import *

connection = SQLC.connect(
             host = 'Localhost',
             user = 'root',
             password = 'SQL12345678',
             database = 'first_database')
cursor = connection.cursor()

#                                                                    MAIN FUNCTIONS

def Insert():
    print("\n(((((INSERT DATA)))))")
    while True:
        try:
            id = int(input("Enter Id: "))
            break
        except ValueError:
            print('(ERROR) "Enter ID Only"')

    name = input("Enter Name: ")
    contact = input("Enter Contact Number: ")
    dept = input("Enter Dept: ")
    cursor.execute(f"insert into 1st_table values({id}, '{name}', '{contact}', '{dept}');")
    connection.commit()

def Update_Name():
    print("\n(((((UPDATE NAME)))))")
    while True:
        try:
            id = int(input("Enter Id: "))
            break
        except ValueError:
            print('(ERROR) "Enter ID Only"')

    name = input("Enter Name: ")
    cursor.execute(f"update 1st_table set Name = '{name}' where ID in ({id});")
    connection.commit()

def Update_Contact():
    print("\n(((((UPDATE CONTACT)))))")
    while True:
        try:
            id = int(input("Enter Id: "))
            break
        except ValueError:
            print('(ERROR) "Enter ID Only"')

    contact = input("Enter Contact Number: ")
    cursor.execute(f"update 1st_table set Contact_Number = '{contact}' where ID in ({id});")
    connection.commit()

def Update_Dept():
    print("\n(((((UPDATE DEPT)))))")
    while True:
        try:
            id = int(input("Enter Id: "))
            break
        except ValueError:
            print('(ERROR) "Enter ID Only"')

    dept = input("Enter Dept: ")
    cursor.execute(f"update 1st_table set Dept = '{dept}' where ID in ({id});")
    connection.commit()

def Delete():
    print("\n(((((DELETE DATA)))))")
    while True:
        try:
            id = int(input("Enter Id: "))
            break
        except ValueError:
            print('(ERROR) "Enter ID Only"')

    cursor.execute(f"DELETE FROM 1st_table WHERE id = {id};")
    connection.commit()

def Find_Name():
    print("\n(((((FIND NAME)))))")
    name = input("Enter Name: ")
    cursor.execute(f"Select * From 1st_table where Name like '%{name}%'")
    fetch = cursor.fetchall()
    print (fetch)

def Find_Contact():
    print("\n(((((FIND CONTACT)))))")
    contact = input("Enter Contact Number: ")
    cursor.execute(f"Select * From 1st_table where Contact_Number like '%{contact}%'")
    fetch = cursor.fetchall()
    print (fetch)

def Find_Dept():
    print("\n(((((FIND DEPT)))))")
    dept = input("Enter Dept: ")
    cursor.execute(f"Select * From 1st_table where Dept like '%{dept}%'")
    fetch = cursor.fetchall()
    print (fetch)

def Read_All():
    label = {'0': 'ID',
             '1': 'Name',
             '2': 'Contact Number',
             '3': 'Dept'}
    
    print("\n(((((ALL DATA)))))\n")
    cursor.execute(f"select * from 1st_table;")
    fetch = cursor.fetchall()

    for row in fetch:
        n = 0
        
        for item in row:
            
            if(n == 0):
                print(f"{label['0']} = {item}")
            elif(n == 1):
                print(f"{label['1']} = {item}")
            elif(n == 2):
                print(f"{label['2']} = {item}")
            elif(n == 3):
                print(f"{label['3']} = {item}")

            n += 1

        print("\n")

def Custom_Query(SQL):

    cursor.execute(SQL)
    connection.commit()

#                                                                    GUI FUNCTIONS

def Insert_Label(text_t, x, y):

    label = Label(
                text = text_t,
                font = 'Montserrat',
                background = 'Red',
                foreground = 'White',
                width = 40 )
    
    label.place( x = x, y = y )

def Insert_Text_Box(x, y):

    text_box = Entry(
                font = "Montserrat",
                background = 'White',
                foreground = 'Black',
                width = 37)
    
    text_box.place(x = x, y = y)

def Insert_Button(text, x, y):

    button = Button(
                text = text,
                font = 'Montserrat',
                background = 'Black',
                foreground = 'White')
    
    button.place (x = x , y = y)
