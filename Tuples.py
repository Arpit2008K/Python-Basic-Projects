class Employee:
    def __init__(self,emp_id, name, details):
        self.emp_id=emp_id
        self.name=name
        self.details=details
    def show_details(self):
        print("Employee id:",self.emp_id)
        print("Name:",self.name)
        print("Details:",self.details)
        print()

e1=Employee(17436,"Rahul",("IT",56000))
e2=Employee(49074,"Rohan",("HR",50000))
e3=Employee(57037,"Sahil",("Physicist",56000))

emp={
    17436:e1,
    49074:e2,
    57037:e3
}
for i in emp:
    emp[i].show_details()
