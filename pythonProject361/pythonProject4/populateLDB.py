from lecturer_table import DatabaseInteraction
from tkinter import END

DBobj = DatabaseInteraction("LecturerDB.db")


class PopulateData:
    def populateListBox(self, gui_app):
        gui_app.plist.delete(0, END)
        if DBobj.fetchData():
            for row in DBobj.fetchData():
                gui_app.plist.insert(END, row)
        else:
            print("Data not fetched from DB")


