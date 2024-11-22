import sqlite3

class DatabaseInteraction:
    # set up constructor and connection to database
    def __init__(self, db):
        self.conn = sqlite3.connect(db) #connection object to database
        self.cursor = self.conn.cursor()    # cursor object to execute queries

        # define CRUD methods
    def insertData(self, id, name, gender, course,stream):
            self.cursor.execute("INSERT INTO Students VALUES (?,?,?,?,?)", ( id, name, gender, course,stream))
            self.conn.commit()

    def fetchData(self):
            self.cursor.execute("SELECT * FROM Students")
            rows = self.cursor.fetchall()   #fetches all rows in a table
            print(rows)
            return rows

    def updateData(self, id, name, gender, course,stream,):
        self.cursor.execute("UPDATE Students SET "
                            " name = ?,"
                            " gender = ?,"
                            " course = ?,"
                            " stream = ? "
                            "WHERE id=?",
                            (id, name, gender, course,stream,))
        self.conn.commit()

    def deleteData(self, id):
        self.cursor.execute("DELETE FROM Students WHERE id=?", (id,))
        self.conn.commit()

 # Destructor
    def __del__(self):
        self.conn.close()



'''
#Create DB
conn = sqlite3.connect("StudentDB.db")
cursor = conn.cursor()
print("Database Created!")
'''
'''
#Create Table
cursor.execute("CREATE TABLE IF NOT EXISTS Students "
               "(id INTEGER PRIMARY KEY,"
               " name TEXT,"
               " gender TEXT,"
               " course TEXT,"
               " stream TEXT)")
conn.commit()
print("Table Created!")
'''
'''
conn = sqlite3.connect("StudentDB.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO Students VALUES (?,?,?,?,?)", ("", "John", "Male", "IT", "Software"))
cursor.execute("INSERT INTO Students VALUES (?,?,?,?,?)", ("", "Ben", "Male", "Law", "Defence"))
cursor.execute("INSERT INTO Students VALUES (?,?,?,?,?)", ("", "Lisa", "Female", "sport Science", "Football"))
conn.commit()


print("Data Inserted!")
cursor.execute("SELECT * FROM Students")
for row in cursor:
    print(row)
'''

