import sqlite3



class DatabaseInteraction:
    # set up constructor and connection to database
    def __init__(self, db):
        self.conn = sqlite3.connect(db) #connection object to database
        self.cursor = self.conn.cursor()    # cursor object to execute queries

        # define CRUD methods
    def insertData(self, li, le, ln, lg, lm):
            self.cursor.execute("INSERT INTO Lecturers VALUES (?,?,?,?,?)", ( li, le, ln, lg, lm,))
            self.conn.commit()

    def fetchData(self):
            self.cursor.execute("SELECT * FROM Lecturers")
            rows = self.cursor.fetchall()   #fetches all rows in a table
            print(rows)
            return rows

    def updateData(self, li, le, ln, lg, lm,):
        self.cursor.execute("UPDATE Lecturers SET "
                            " name= ?,"
                            " email = ?,"
                            " gender = ?,"
                            " modules = ?"
                            "WHERE id=?",
                            (  li, le, ln, lg, lm,))
        self.conn.commit()

    def deleteData(self, id):
        self.cursor.execute("DELETE FROM Lecturers WHERE id=?", (id,))
        self.conn.commit()

 # Destructor
    def __del__(self):
        self.conn.close()
        

        

'''
#Create lecturer database
conn = sqlite3.connect("LecturerDB.db")
cursor = conn.cursor()
print("Lecturer Database Created!")

cursor.execute('ALTER TABLE Lecturers ADD COLUMN email TEXT')

cursor.execute("CREATE TABLE IF NOT EXISTS Lecturers"
               "(id INTEGER PRIMARY KEY,"
               " name TEXT,"
               " gender TEXT,"
               " email TEXT,"
               " modules TEXT)")

conn.commit()
print("Lecturer Table Created!")
conn.close()

'''


'''
conn = sqlite3.connect("LecturerDB.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO Lecturers VALUES(?,?,?,?,?)", (None, 'Simba Zengeni', 'Male', 'SSX361, WPR261, PRJ361'))
cursor.execute("INSERT INTO Lecturers VALUES(?,?,?,?,?)", (None, 'Ikraam Sadek', 'Male', 'PRG161'))
cursor.execute("INSERT INTO Lecturers VALUES(?,?,?,?,?)",  (None, 'Matilda Chiruka', 'Female', 'MAT161, STA161'))

conn.commit()
print("Data Inserted!")

conn = sqlite3.connect("LecturerDB.db")
cursor = conn.execute("SELECT * FROM Lecturers")

for row in cursor:
    print(row)

'''
