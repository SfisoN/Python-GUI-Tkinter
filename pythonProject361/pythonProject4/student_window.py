
from tkinter import *
from add_student import AddStudent
from update_student import UpdateStudent
from delete_student import DeleteStudent
from populateDB import PopulateData

class StudentWindow:
    def __init__(self, root):
        self.root = root


    def add_widgets(self):
        self.idtxt = StringVar()
        self.ntxt = StringVar()
        self.gtxt = StringVar()
        self.ctxt = StringVar()
        self.sttxt = StringVar()
        self.index = StringVar()
        self.index = NONE

        # Student ID
        idlabel = Label(self.root, text="Student ID: ", font=("Bold", 12), pady=10)
        idlabel.grid(row=0, column=0, sticky=W, padx=10)
        self.idtextbox = Entry(self.root, textvariable=self.idtxt)
        self.idtextbox.grid(row=0, column=1, padx=10, pady=10)

        # Student Name
        nlabel = Label(self.root, text="Student Full Name: ", font=("Bold", 12), pady=10)
        nlabel.grid(row=1, column=0, sticky=W, padx=10)
        self.ntextbox = Entry(self.root, textvariable=self.ntxt)
        self.ntextbox.grid(row=1, column=1, padx=10, pady=10)

        # Gender
        glabel = Label(self.root, text="Gender: ", font=("Bold", 12), pady=10)
        glabel.grid(row=2, column=0, sticky=W, padx=10)
        self.gtextbox = Entry(self.root, textvariable=self.gtxt)
        self.gtextbox.grid(row=2, column=1, padx=10, pady=10)

        # Course
        clabel = Label(self.root, text="Course: ", font=("Bold", 12), pady=10)
        clabel.grid(row=3, column=0, sticky=W, padx=10)
        self.ctextbox = Entry(self.root, textvariable=self.ctxt)
        self.ctextbox.grid(row=3, column=1, padx=10, pady=10)

        #Stream
        slabel = Label(self.root, text="Stream: ", font=("Bold", 12), pady=10)
        slabel.grid(row=3, column=2, sticky=W, padx=10)
        self.stextbox = Entry(self.root, textvariable=self.sttxt)
        self.stextbox.grid(row=3, column=3, padx=10, pady=10)

        # Buttons
        add_btn = Button(self.root, text="Add Student", width=12, command=self.add_student)
        add_btn.grid(row=4, column=0, pady=20, padx=10)

        update_btn = Button(self.root, text="Update Student", width=12, command=self.update_student)
        update_btn.grid(row=4, column=1, pady=20)

        delete_btn = Button(self.root, text="Delete Student", width=12, command=self.delete_student)
        delete_btn.grid(row=4, column=2, pady=20)

        clear_btn = Button(self.root, text="Clear Student", width=12, command=self.clear_textbox)
        clear_btn.grid(row=4, column=3, pady=20)

        # Listbox
        self.plist = Listbox(self.root, height=10, width=70)
        self.plist.grid(row=5, column=0, columnspan=4, rowspan=6, pady=20, padx=10)
        self.plist.bind("<<ListboxSelect>>", self.on_select)


#Button to load data in db
        reload_btn = Button(self.root, text="Reload Data", width=12, command=self.populate)
        reload_btn.grid(row=11, column=1, pady=20, padx=20)


        # Function to clear all textboxes
    def clear_textbox(self):
            self.idtxt.set("")
            self.ntxt.set("")
            self.gtxt.set("")
            self.ctxt.set("")
            self.sttxt.set("")



        # Function in Listbox
    def on_select(self, event):
        global selected_item
        index = self.plist.curselection()[0]
        selected_item = self.plist.get(index)

        self.idtextbox.delete(0, END)
        self.idtextbox.insert(END, selected_item[0])
        self.ntextbox.delete(0, END)
        self.ntextbox.insert(END, selected_item[1])
        self.gtextbox.delete(0, END)
        self.gtextbox.insert(END, selected_item[2])
        self.ctextbox.delete(0, END)
        self.ctextbox.insert(END, selected_item[3])
        self.stextbox.delete(0, END)
        self.stextbox.insert(END, selected_item[4])


    '''
            index = self.plist.curselection()
            if index:
                selected_item = self.plist.get(index)
                details = selected_item.split(" - ")
                self.idtxt.set(details[0])
                self.ntxt.set(details[1])
                self.gtxt.set(details[2])
                self.ctxt.set(details[3])
                self.sttxt.set(details[4])
                '''

        # Instantiate methods that are redefined in Add,Update,Delete_student class
    def add_student(self):
        AddStudent().add_student(self)
        StudentWindow.populate(self)

    def update_student(self):
        UpdateStudent().update_student(self, selected_item[0])

    def delete_student(self):
        DeleteStudent().delete_student(self, selected_item[0])

    def populate(self):
            PopulateData().populateListBox(self)