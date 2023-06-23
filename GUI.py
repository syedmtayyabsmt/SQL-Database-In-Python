from tkinter import *
import Functions

#                                                                    WINDOW

window = Tk()
window.title("SQL DATABASE")
window.geometry('1370x768')
window.config( bg = 'dark gray')

#                                                                    LABELS

Functions.Insert_Label('INSERT DATA', 20, 20)
Functions.Insert_Label('UPDATE DATA', 20, 120)
Functions.Insert_Label('DELETE DATA', 20, 220)
Functions.Insert_Label('FIND DATA', 20, 320)
Functions.Insert_Label('READ ALL DATA', 20, 420)
Functions.Insert_Label('ENTER  CUSTOM  SQL  QUERY', 20, 520)

#                                                                    TEXT BOX

Functions.Insert_Text_Box(20, 50)
Functions.Insert_Text_Box(20, 150)
Functions.Insert_Text_Box(20, 250)
Functions.Insert_Text_Box(20, 350)
Functions.Insert_Text_Box(20, 450)
Functions.Insert_Text_Box(20, 550)

#                                                                    BUTTON

Functions.Insert_Button('INSERT DATA', 20, 80)
Functions.Insert_Button('UPDATE DATA', 20, 180)
Functions.Insert_Button('DELETE DATA', 20, 280)
Functions.Insert_Button('FIND DATA', 20, 380)
Functions.Insert_Button('READ ALL DATA', 20, 480)
Functions.Insert_Button('ENTER  CUSTOM  SQL  QUERY', 20, 580)







window.mainloop()
print ('''=======================================================================================================================================
                             (((((((((((((((((((((((((((( APPLICATION CLOSED ))))))))))))))))))))))))))))
=======================================================================================================================================''')
