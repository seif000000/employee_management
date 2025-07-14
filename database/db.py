import sqlite3

class Database:
    def __init__(self, db_name='employee.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_employees_table()
    def create_employees_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                job_title TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL,
                hire_date TEXT,
                is_active INTEGER NOT NULL DEFAULT 1
            )
            ''')
        self.connection.commit()    
    def get_connection(self):
        return self.connection
    def get_cursor(self):
        return self.cursor
    def close(self):
        self.connection.close()    