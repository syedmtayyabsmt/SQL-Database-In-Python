import Functions

#                                                                    (((MAIN PROGRAM)))


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
        Functions.Insert()
        print("\n==(DATA INSERTED SUCCESSFULLY)==\n")

#                                                                    UPDATE

    elif (user_input == 2):
        print('''What Do You Want To Update ?
Enter (1) For Name
Enter (2) For Contact Number
Enter (3) For Dept''')
        
        update = int(input("Enter Option: "))

        if (update == 1):
            Functions.Update_Name()
            print("\n==(DATA UPDATED SUCCESSFULLY)==\n")


        elif (update == 2):
            Functions.Update_Contact()
            print("\n==(DATA UPDATED SUCCESSFULLY)==\n")
        
        elif (update == 3):
            Functions.Update_Dept()
            print("\n==(DATA UPDATED SUCCESSFULLY)==\n")

        else:
            while(update != 1 and update != 2 and update != 3):
                update = int(input("Enter The Right Value. Type (1) To Update Name, Type (2) To Update Contact, Type (3) To Update Dept: "))

                if (update == 1):
                    Functions.Update_Name()
                    print("\n==(DATA UPDATED SUCCESSFULLY)==\n")

                elif (update == 2):
                    Functions.Update_Contact()
                    print("\n==(DATA UPDATED SUCCESSFULLY)==\n")
                
                elif (update == 3):
                    Functions.Update_Dept()
                    print("\n==(DATA UPDATED SUCCESSFULLY)==\n")

#                                                                    DELETE

    elif (user_input == 3):
        Functions.Delete()
        print("\n==(DATA DELETED SUCCESSFULLY)==\n")

#                                                                    FIND

    elif (user_input == 4):
        print('''What Do You Want To Find ?
Enter (1) For Name
Enter (2) For Contact Number
Enter (3) For Dept''')
        
        find = int(input("Enter Option: "))

        if (find == 1):
            Functions.Find_Name()
            print("\n==(DATA FOUND)==\n")

        elif (find == 2):
            Functions.Find_Contact()
            print("\n==(DATA FOUND)==\n")
        
        elif (find == 3):
            Functions.Find_Dept()
            print("\n==(DATA FOUND)==\n")

        else:
            while (find != 1 and find != 2 and find != 3):
                find = int(input("Enter The Right Value. Type (1) To Find Name, Type (2) To Find Contact, Type (3) To Find Dept: "))

                if (find == 1):
                    Functions.Find_Name()
                    print("\n==(DATA FOUND)==\n")

                elif (find == 2):
                    Functions.Find_Contact()
                    print("\n==(DATA FOUND)==\n")
                
                elif (find == 3):
                    Functions.Find_Dept()
                    print("\n==(DATA FOUND)==\n")

#                                                                    READ ALL DATA

    elif (user_input == 5):
        Functions.Read_All()

#                                                                    EXIT FROM MENU

    elif (user_input == 6):
        break

    else:
        continue

#                                                                    EXIT FROM QUESTION

    exit = input("Do You Want To Exit ? Type (Y) To Exit, Type (N) For Database Operations: ").capitalize()

    if (exit == 'Y'):
        Functions.connection.close()
        break

    elif (exit == 'N'):
        continue

    else:
        while(exit != 'Y' and exit != 'N'):
            exit = input("Enter The Right Value. Type (Y) To Exit, Type (N) For Database Operations: ").capitalize()

            if (exit == 'Y'):
                Functions.connection.close()
                break
            elif (exit == 'N'):
                continue


print("\n==========================")
print("==( PROGRAM TERMINATED )==")
print("==========================\n")
