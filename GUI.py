from tkinter import *
import Functions

#                                                                    WINDOW

window = Tk()
window.title("SQL DATABASE")
window.geometry('1370x768')
window.config( bg = 'dark gray')



menu = '''
===================================================
What Operation Do You Want To Perform On Database ?
===================================================
Enter (1) To Insert Data

Enter (2) To Update Data

Enter (3) To Delete Data

Enter (4) To Find In Data

Enter (5) To Read All Data

Enter (6) To Enter Custom SQL Query

Enter (7) To Exit'''

label = Label(
            text = menu,
            font = 'Montserrat',
            background = 'Red',
            foreground = 'White',
            width = 130)
label.place( x = 20, y = 20 )


# Text Box
text_box = Entry(
                font = "Montserrat",
                background = 'White',
                foreground = 'Black',
                width = 118)
text_box.place(x = 20, y = 450)

# Button
button = Button(
                text = "ENTER OPERATION",
                font = 'Montserrat',
                background = 'Black',
                foreground = 'White')
button.place(x = 570, y = 500)
    



print(text_box.get())










window.mainloop()
print ('''=======================================================================================================================================
                             (((((((((((((((((((((((((((( APPLICATION CLOSED ))))))))))))))))))))))))))))
=======================================================================================================================================''')
