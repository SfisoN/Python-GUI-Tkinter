from tkinter import *
from add_lecturer import AddLecturer
from delete_lecturer import DeleteLecturer
from update_lecturer import UpdateLecturer
from populateLDB import PopulateData


class LecturerWindow:
    def __init__(self, root):
        self.root = root

    def add_widgets(self):
        self.idtxt = StringVar()
        self.etxt = StringVar()
        self.ntxt = StringVar()
        self.gtxt = StringVar()
        self.mtxt = StringVar()
        self.index = StringVar()
        self.index = NONE


        id_label = Label(self.root, text="Lecturer ID: ", font=("Bold", 12), pady=20)
        id_label.grid(row=0, column=0, sticky=E, padx=10)
        self.idtextbox = Entry(self.root, textvariable=self.idtxt)
        self.idtextbox.grid(row=0, column=1, padx=10, pady=10)

        email_label = Label(self.root, text="Email: ", font=("Bold", 12), pady=20)
        email_label.grid(row=0, column=2, sticky=E, padx=10)
        self.etextbox = Entry(self.root, textvariable=self.etxt)
        self.etextbox.grid(row=0, column=3, padx=10, pady=10)

        name_label = Label(self.root, text="Lecturer Full Name: ", font=("Bold", 12), pady=20)
        name_label.grid(row=1, column=0, sticky=E, padx=10)
        self.ntextbox = Entry(self.root, textvariable=self.ntxt)
        self.ntextbox.grid(row=1, column=1, padx=10, pady=10)

        #Gender
        gender_label = Label(self.root, text="Gender: ", font=("Bold", 12), pady=20)
        gender_label.grid(row=2, column=0, sticky=E, padx=10)
        self.gtextbox = Entry(self.root, textvariable=self.gtxt)
        self.gtextbox.grid(row=2, column=1, padx=10, pady=10)

        module_label = Label(self.root, text="Modules: ", font=("Bold", 12), pady=20)
        module_label.grid(row=1, column=2, sticky=E, padx=10)
        self.mtextbox = Entry(self.root, textvariable=self.mtxt)
        self.mtextbox.grid(row=1, column=3)

        # Buttons
        add_btn = Button(self.root, text="Add Lecturer", width=12, command=self.add_lecturer)
        add_btn.grid(row=4, column=0, pady=20, padx=10)

        update_btn = Button(self.root, text="Update Lecturer", width=12, command=self.update_lecturer)
        update_btn.grid(row=4, column=1, pady=20)

        delete_btn = Button(self.root, text="Delete Lecturer", width=12, command=self.delete_lecturer)
        delete_btn.grid(row=4, column=2, pady=20)

        clear_btn = Button(self.root, text="Clear Lecturer", width=12, command=self.clear_textbox)
        clear_btn.grid(row=4, column=3, pady=20)

        # Listbox
        self.plist = Listbox(self.root, height=10, width=70)
        self.plist.grid(row=5, column=0, columnspan=4, rowspan=6, pady=20, padx=10)
        self.plist.bind("<<ListboxSelect>>", self.on_select)


        reload_btn = Button(self.root, text="Reload Data", width=12, command=self.populate)
        reload_btn.grid(row=11, column=1, pady=20, padx=20)

        # Function to clear all textboxes

    def clear_textbox(self):
        self.idtxt.set("")
        self.etxt.set("")
        self.ntxt.set("")
        self.gtxt.set("")
        self.mtxt.set("")


        # Function in Listbox

    def on_select(self, event):
        global selected_item
        index = self.plist.curselection()
        selected_item = self.plist.get(index)

        self.idtextbox.delete(0, END)
        self.idtextbox.insert(END, selected_item[0])
        self.etextbox.delete(0, END)
        self.etextbox.insert(END, selected_item[1])
        self.ntextbox.delete(0, END)
        self.ntextbox.insert(END, selected_item[2])
        self.gtextbox.delete(0, END)
        self.gtextbox.insert(END, selected_item[3])
        self.mtextbox.delete(0, END)
        self.mtextbox.insert(END, selected_item[4])

        '''
        index = self.plist.curselection()
        if index:
            selected_item = self.plist.get(index)
            details = selected_item.split(" - ")
            self.idtxt.set(details[5])
            self.ntxt.set(details[3])
            self.mtxt.set(details[4])
            self.etxt.set(details[6])
            '''

        # Instantiate methods that are redefined in Add,Update,Delete_student class

    def add_lecturer(self):
        AddLecturer().add_lecturer(self)
        LecturerWindow.populate(self)

    def update_lecturer(self):
        UpdateLecturer().update_lecturer(self, selected_item[0])

    def delete_lecturer(self):
        DeleteLecturer().delete_lecturer(self, selected_item[0])

    def populate(self):
            PopulateData().populateListBox(self)