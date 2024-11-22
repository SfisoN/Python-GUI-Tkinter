from  tkinter import END
from student_table import DatabaseInteraction

dbObj = DatabaseInteraction("StudentDB.db")

class AddStudent:
    def add_student(self, gui_app):


        idtxt = gui_app.idtxt.get()
        ntxt = gui_app.ntxt.get()
        gtxt = gui_app.gtxt.get()
        ctxt = gui_app.ctxt.get()
        sttxt = gui_app.sttxt.get()


        if idtxt and ntxt and gtxt and ctxt and sttxt:
            gui_app.plist.delete(0, END)
            dbObj.insertData(idtxt, ntxt, gtxt, ctxt, sttxt)
            gui_app.clear_textbox()
        else:
            print("Please fill all fields!")



'''
 if idtxt and ntxt and gtxt and ctxt and sttxt:
            student_info = f"{gui_app.idtxt.get()} - {gui_app.ntxt.get()} - {gui_app.gtxt.get()} -{gui_app.ctxt.get()} - {gui_app.sttxt.get()}"
            gui_app.plist.insert(END, student_info)
            gui_app.clear_textbox()
        else:
            print("Please fill all fields!")
            
            '''
