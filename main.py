import mysql.connector as SQLC


#                                                                    FUNCTIONS

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

#                                                                    (((MAIN PROGRAM)))

connection = SQLC.connect(
             host = 'Localhost',
             user = 'root',
             password = 'SQL12345678',
             database = 'first_database')
cursor = connection.cursor()


while (exit != 'Y'):

    print("\n===================================================")
    print("What Operation Do You Want To Perform On Database ?")
    print("===================================================\n")
    print('Enter (1) To Insert Data')
    print('Enter (2) To Update Data')
    print('Enter (3) To Delete Data')
    print('Enter (4) To Find In Data')
    print('Enter (5) To Read All Data')
    print('Enter (6) To Exit\n')

    while(True):
    
        try:
            user_input = int(input('Enter Option: '))
            break
        except ValueError:
            print('(ERROR) "Enter Number Only"')


#                                                                    INSERT

    if (user_input == 1):
        Insert()
        print("\n==(DATA INSERTED SUCCESSFULLY)==\n")

#                                                                    UPDATE

    elif (user_input == 2):
        print('''What Do You Want To Update ?
Enter (1) For Name
Enter (2) For Contact Number
Enter (3) For Dept''')
        
        update = int(input("Enter Option: "))

        if (update == 1):
            Update_Name()
            print("\n==(DATA UPDATED SUCCESSFULLY)==\n")


        elif (update == 2):
            Update_Contact()
            print("\n==(DATA UPDATED SUCCESSFULLY)==\n")
        
        elif (update == 3):
            Update_Dept()
            print("\n==(DATA UPDATED SUCCESSFULLY)==\n")

        else:
            while(update != 1 and update != 2 and update != 3):
                update = int(input("Enter The Right Value. Type (1) To Update Name, Type (2) To Update Contact, Type (3) To Update Dept: "))

                if (update == 1):
                    Update_Name()
                    print("\n==(DATA UPDATED SUCCESSFULLY)==\n")

                elif (update == 2):
                    Update_Contact()
                    print("\n==(DATA UPDATED SUCCESSFULLY)==\n")
                
                elif (update == 3):
                    Update_Dept()
                    print("\n==(DATA UPDATED SUCCESSFULLY)==\n")

#                                                                    DELETE

    elif (user_input == 3):
        Delete()
        print("\n==(DATA DELETED SUCCESSFULLY)==\n")

#                                                                    FIND

    elif (user_input == 4):
        print('''What Do You Want To Find ?
Enter (1) For Name
Enter (2) For Contact Number
Enter (3) For Dept''')
        
        find = int(input("Enter Option: "))

        if (find == 1):
            Find_Name()
            print("\n==(DATA FOUND)==\n")

        elif (find == 2):
            Find_Contact()
            print("\n==(DATA FOUND)==\n")
        
        elif (find == 3):
            Find_Dept()
            print("\n==(DATA FOUND)==\n")

        else:
            while (find != 1 and find != 2 and find != 3):
                find = int(input("Enter The Right Value. Type (1) To Find Name, Type (2) To Find Contact, Type (3) To Find Dept: "))

                if (find == 1):
                    Find_Name()
                    print("\n==(DATA FOUND)==\n")

                elif (find == 2):
                    Find_Contact()
                    print("\n==(DATA FOUND)==\n")
                
                elif (find == 3):
                    Find_Dept()
                    print("\n==(DATA FOUND)==\n")

#                                                                    READ ALL DATA

    elif (user_input == 5):
        Read_All()

#                                                                    EXIT FROM MENU

    elif (user_input == 6):
        break

    else:
        continue

#                                                                    EXIT FROM QUESTION

    exit = input("Do You Want To Exit ? Type (Y) To Exit, Type (N) For Database Operations: ").capitalize()

    if (exit == 'Y'):
        connection.close()
        break

    elif (exit == 'N'):
        continue

    else:
        while(exit != 'Y' and exit != 'N'):
            exit = input("Enter The Right Value. Type (Y) To Exit, Type (N) For Database Operations: ").capitalize()

            if (exit == 'Y'):
                connection.close()
                break
            elif (exit == 'N'):
                continue


print("\n==========================")
print("==( PROGRAM TERMINATED )==")
print("==========================\n")
