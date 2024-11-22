from tkinter import END
from student_table import DatabaseInteraction

dbObj = DatabaseInteraction("StudentDB.db")

class UpdateStudent:
    def update_student(self, gui_app,id):

        id = gui_app.idtxt.get()
        name = gui_app.ntxt.get()
        gender = gui_app.gtxt.get()
        course = gui_app.ctxt.get()
        stream = gui_app.sttxt.get()

        if id and name and gender and course and stream:
            gui_app.plist.delete(0, END)
            dbObj.updateData(id, name, gender, course, stream,)
            gui_app.clear_textbox()
        else:
            print("Select a field to update!")


        '''
        index = gui_app.plist.curselection()
        if index:
            # Extract the first selected index
            selected_index = index[0]
            updated_details = f"{gui_app.idtxt.get()} - {gui_app.ntxt.get()} - {gui_app.gtxt.get()}- {gui_app.ctxt.get()} - {gui_app.sttxt.get()} "
            gui_app.plist.delete(selected_index)
            gui_app.plist.insert(selected_index, updated_details)
            gui_app.clear_textbox()
        else:
            print("Select an item to update!")
        '''
