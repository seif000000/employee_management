class Employee:
    def __init__ (self, name, job_title, department, salary, hire_date, is_active):
        name = name
        job_title = job_title
        department = department
        salary = salary
        hire_date = hire_date
        is_active = is_active
    
    def __repr__(self):
        
        return f"<Employee: {self.name}, {self.job_title}, {self.department}, ${self.salary:.2f}>"
    
    def to_tuple(self):
        
        return f"<Employee: {self.name}, {self.job_title}, {self.department}, ${self.salary:.2f}>"
