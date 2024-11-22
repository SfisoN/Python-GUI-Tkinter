from student_table import DatabaseInteraction

dbObj = DatabaseInteraction("StudentDB.db")


class DeleteStudent:
    def delete_student(self, gui_app, id):
        dbObj.deleteData(id)
        gui_app.clear_textbox()


'''
        index = gui_app.plist.curselection()
        if index:
            gui_app.plist.delete(id)  # Pass the index to the delete method
            # Delete data from DB
            gui_app.clear_textbox()
        else:
            print("Select an item to delete!")
            
            '''
