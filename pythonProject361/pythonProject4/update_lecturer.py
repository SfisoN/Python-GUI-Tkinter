from lecturer_table import DatabaseInteraction
from tkinter import END

DBobj = DatabaseInteraction("LecturerDB.db")


class UpdateLecturer:
    def update_lecturer(self, gui_app, id):
        li = gui_app.idtxt.get()
        le = gui_app.etxt.get()
        ln = gui_app.ntxt.get()
        lg = gui_app.gtxt.get()
        lm = gui_app.mtxt.get()

        if li and le and ln and lg and lm:
            gui_app.plist.delete(0, END)
            DBobj.updateData(li, le, ln, lg, lm)
            gui_app.clear_textbox()
        else:
            print("Select a field to update!")


        '''
        index = gui_app.plist.curselection()
        if index:
            selected_item = gui_app.plist.get(index)
            updated_details = f"{gui_app.ntxt.get()} - {gui_app.mtxt.get()} - {gui_app.idtxt.get()} - {gui_app.sttxt.get()} - {gui_app.ctxt.get()}"
            gui_app.plist.delete(index)
            gui_app.plist.insert(index, selected_item, updated_details)
            gui_app.clear_textbox()
        else:
            print("Select an item to update!")
            '''
