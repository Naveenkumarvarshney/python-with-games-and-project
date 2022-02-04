# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=f"{self.fname+self.lname}@naveen.com"

#     @property
#     def email(self):
#         if self.fname==None or self.lname==None:
#             return f"error"

#         return f"{self.fname+self.lname}@gmail.com"

#     @email.setter
#     def email(self,String):
#         name= String.split('@')
#         self.fname=name[0]

#     @email.deleter
#     def email(self):
#         self.fname=None
#         self.lname=None


# obj1=Employee("Tinku","Varshney2014")
# string="My name is naveen"

# # Method 1:It give the id of the object
# # print(id(obj1))
# # print(id(string))

# #Method 2: It gives information on all the attributes of the object in the class 
# # print(dir(obj1))
# # print(dir(string))

# # Method 3: it gives the information of attributes and its value in the class 
# import inspect
# g=inspect.getmembers(obj1)
# print(g)



# program on object introspection:


import inspect
class Human:
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname 
    def explain(self):
        return f"this is {self.fname} {self.lname}" 
    @property   
    def inspection(self):
        a = inspect.isclass(Human)
        print ("Identify that it's a class or not: ")
        if a == True:
            print("It's a class.")
        else:
            print("It's not a class !!")
    

human = Human("Haris","Khan")
human.inspection