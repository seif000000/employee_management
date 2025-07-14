# services/employee_service.py

from database.db import Database  

class EmployeeService:
    def __init__(self):
        self.db = Database()  

    def add_employee(self, name, job_title, department, salary):
        cursor = self.db.get_cursor()
        query = "INSERT INTO employees (name, job_title, department, salary) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (name, job_title, department, salary))
        self.db.get_connection().commit()


    def get_all_employees(self):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM employees")
        return cursor.fetchall()  

    def update_employee(self, emp_id, name=None, job_title=None, department=None, salary=None):
        cursor = self.db.get_cursor()
        fields = []
        values = []
    
        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if job_title is not None:
            fields.append("job_title = ?")
            values.append(job_title)
        if department is not None:
            fields.append("department = ?")
            values.append(department)
        if salary is not None:
            fields.append("salary = ?")
            values.append(salary)
    
        if not fields:
            return
    
        values.append(emp_id)
        query = f"UPDATE employees SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(query, values)
        self.db.get_connection().commit()


    def delete_employee(self, emp_id):
        cursor = self.db.get_cursor()
        query = "DELETE FROM employees WHERE id = ?"
        cursor.execute(query, (emp_id,))
        self.db.get_connection().commit()

    def search_by_name(self, name):
        cursor = self.db.get_cursor()
        query = "SELECT * FROM employees WHERE name LIKE ?"
        cursor.execute(query, (f"%{name}%",))
        return cursor.fetchall()
