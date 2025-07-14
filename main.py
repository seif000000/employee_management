from services.employee_service import EmployeeService

def main():
    service = EmployeeService()

    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Add New Employee")
        print("2. Show All Employees")
        print("3. Update Employee Info")
        print("4. Delete Employee")
        print("5. Search Employee by Name")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Employee Name: ")
            job_title = input("Job Title: ")
            department = input("Department: ")
            salary = float(input("Salary: "))
            service.add_employee(name, job_title, department, salary)
            print("Employee added successfully!")


        elif choice == '2':
            employees = service.get_all_employees()
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Job Title: {emp[2]}, Department: {emp[3]}, Salary: {emp[4]}")

        elif choice == '3':
            emp_id = int(input("Enter employee ID to update: "))
            name = input("New name (or leave empty): ")
            job_title = input("New job title (or leave empty): ")
            department = input("New department (or leave empty): ")
            salary_input = input("New salary (or leave empty): ")

            name = name if name else None
            job_title = job_title if job_title else None
            department = department if department else None
            salary = float(salary_input) if salary_input else None
            # يعني لو المستخدم كتب حاجه عدلها لو مكتبش اكتب none او متدلش 

            service.update_employee(emp_id, name, job_title, department, salary)
            print("Employee updated successfully!")


        elif choice == '4':
            emp_id = int(input("Enter employee ID to delete: "))
            service.delete_employee(emp_id)
            print("Employee deleted successfully!")

        elif choice == '5':
            name = input("Enter employee name to search: ")
            results = service.search_by_name(name)
            for emp in results:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Job Title: {emp[2]}, Department: {emp[3]}, Salary: {emp[4]}")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
