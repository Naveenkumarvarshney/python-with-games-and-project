
# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=f"{self.fname+self.lname}@naveen.com"

#     @property
#     def email(self):
#         return f"{self.fname+self.lname}@naveen.com"

    

# obj1=Employee("Tinku","Varshney")
# obj1.fname="naveen"
# print(obj1.email)


# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=f"{self.fname+self.lname}@naveen.com"

#     @property
#     def email(self):
#         return f"{self.fname+self.lname}@gmail.com"

#     @email.setter
#     def email(self,String):
#         name= String.split('@')
#         self.fname=name[0]

# obj1=Employee("Tinku","Varshney2014")
# print(obj1.email)
# obj1.email="naveen@gmail.com"
# print(obj1.email)

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname+self.lname}@naveen.com"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return f"error"

        return f"{self.fname+self.lname}@gmail.com"

    @email.setter
    def email(self,String):
        name= String.split('@')
        self.fname=name[0]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


obj1=Employee("Tinku","Varshney2014")
print(obj1.email)
obj1.email="naveen@gmail.com"
print(obj1.email)

del obj1.email
print(obj1.email)