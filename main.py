class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    @staticmethod
    def sort_employees(employees, sort_param):
        if sort_param == 1: 
            return sorted(employees, key=lambda emp: emp.age)
        elif sort_param == 2:  
            return sorted(employees, key=lambda emp: emp.name)
        elif sort_param == 3:  
            return sorted(employees, key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter.")
            return employees


employees_data = [
    ("161E90", "Raman", 41, 56000),
    ("161F91", "Himadri", 38, 67500),
    ("161F99", "Jaya", 51, 82100),
    ("171E20", "Tejas", 30, 55000),
    ("171G30", "Ajay", 45, 44000),
]


employees = [Employee(emp_id, name, age, salary) for emp_id, name, age, salary in employees_data]


print("Enter the sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")
sort_param = int(input("Choose a sorting parameter: "))

sorted_employees = Employee.sort_employees(employees, sort_param)
for employee in sorted_employees:
    print(employee)
