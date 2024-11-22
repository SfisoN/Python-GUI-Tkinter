from lecturer_table import DatabaseInteraction

DBobj = DatabaseInteraction("LecturerDB.db")


class DeleteLecturer:
    def delete_lecturer(self, gui_app, id):
        DBobj.deleteData(id)
        gui_app.clear_textbox()


        '''
        index = gui_app.plist.curselection()
        if index:
            gui_app.plist.delete(index)
            gui_app.clear_textbox()
        else:
            print("Select a lecturer to delete!")
        '''