class teacher:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def name(self):
        print("the teacher name is : "+self.firstname+ " "+self.lastname)    

    def joinyear(self,year):
        print("the joining year is : "+format(year)+self.firstname)  

class student(teacher):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        # teacher.__init__(self,fname,lname)
        self.year=year


    def enteringyear(self,year):
        print("The entering year is :  "+ format(year))    

    def newname(self):
        print(self.firstname+self.lastname)


p=student("naveen","varshney",2019)   
p.enteringyear(2019) 
p.joinyear(2019)
p.name()
p.newname()



# q=student("naveen","varshney")
# q.name()
# q.joinyear("five")
         
        
