from student_table import DatabaseInteraction
from tkinter import END

dbObj = DatabaseInteraction("StudentDB.db")

class PopulateData:
    def populateListBox(self, gui_app):
        gui_app.plist.delete(0, END)
        if dbObj.fetchData():
            for row in dbObj.fetchData():
                gui_app.plist.insert(END, row)
        else:
            print("Data not fetched from DB")


