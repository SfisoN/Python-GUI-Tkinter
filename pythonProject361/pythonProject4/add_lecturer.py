from tkinter import END
from lecturer_table import DatabaseInteraction

DBobj = DatabaseInteraction("LecturerDB.db")


class AddLecturer:
    def add_lecturer(self, gui_app):
        li = gui_app.idtxt.get()
        le = gui_app.etxt.get()
        ln = gui_app.ntxt.get()
        lg = gui_app.gtxt.get()
        lm = gui_app.mtxt.get()

        if li and le and ln and lg and lm:
            gui_app.plist.delete(0, END)
            DBobj.insertData(li, le, ln, lg, lm)
            gui_app.clear_textbox()
        else:
            print("Please fill in all Lecturer fields!")

    '''
        if lecturer_id and lecturer_email and lecturer_name and lecturer_gender and lecturer_modules:
            lecturer_info = f"{lecturer_id} - {lecturer_email} - {lecturer_name} - {lecturer_gender} - {lecturer_modules}"
            gui_app.plist.insert(END, lecturer_info)
            #send to DB
            gui_app.clear_textbox()
        else:
            print("Please fill in all fields!")
            '''
