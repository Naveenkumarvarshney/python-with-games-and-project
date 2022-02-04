class Employee:
    def printEmployeedetail(self):
        print(f"the name is {self.name} and the salary is {self.salary}")



naveen=Employee()
naveen.salary=40
naveen.branch="it"
naveen.name="naveen"

harry=Employee()
harry.salary=50
harry.branch="it"
harry.name="harry"

naveen.printEmployeedetail()
harry.printEmployeedetail()