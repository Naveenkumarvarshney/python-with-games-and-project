class Employee:
    newclassh =8
    def __init__(self,name,salary):
        self.aname=name
        self.asalary=salary

    def printEmployeedetail(self):
        print(f"the name is {self.aname} and the salary is {self.asalary}")

    @staticmethod
    def printitem():
        print(f"hello how are you ")

    @classmethod
    def newclass(cls,leaves):
        cls.newclassh=leaves



naveen=Employee("naveen",40)
# naveen.newclassh=10

# print(Employee.newclassh)
# print(naveen.newclassh)
# naveen.printEmployeedetail()
# naveen.printitem()
naveen.newclass(34)
print(naveen.newclassh)