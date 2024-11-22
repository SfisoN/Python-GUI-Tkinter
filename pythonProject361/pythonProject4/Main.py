import tkinter as tk
from student_window import StudentWindow
from lecturer_window import LecturerWindow
 





# Function to open Student window
def open_student_window():
    student_window = tk.Toplevel()
    student_window.title("Student Window")
    student_window.geometry("650x550")
    student_window.configure(bg='light grey')
    student_app = StudentWindow(student_window)
    student_app.add_widgets()
    student_window.mainloop()



# Function to open Lecturer window
def open_lecturer_window():
    lecturer_window = tk.Toplevel()
    lecturer_window.title("Lecturer Window")
    lecturer_window.geometry("650x550")
    lecturer_window.configure(bg='light grey')

    lecturer_app = LecturerWindow(lecturer_window)
    lecturer_app.add_widgets()
    lecturer_window.mainloop()


# Main application window
def main():
    root = tk.Tk()
    root.title("Welcome Page")
    root.geometry("750x500")
    root.configure(bg='grey')


    # Welcome Label
    welcome_label = tk.Label(root, text="Welcome to the University Portal", font=("Helvetica", 16, "bold"), bg='grey')
    welcome_label.pack(pady=20)

    # Student Button
    student_button = tk.Button(root, text="Open Student Window", command=open_student_window, font=("Helvetica", 12, "bold"), bg='orange', fg='white', width=25, height=3)
    student_button.pack(pady=10)


    # Lecturer Button
    lecturer_button = tk.Button(root, text="Open Lecturer Window", command=open_lecturer_window, font=("Helvetica", 12, "bold"), bg='green', fg='white', width=25, height=3)
    lecturer_button.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()



if __name__ == "__main__":
    main()