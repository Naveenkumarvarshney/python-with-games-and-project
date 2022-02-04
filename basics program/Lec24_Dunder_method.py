# __se shuru hone wale aur __ khatam hone wale method ko Dunder method kahate h
# Ex - __init__,__add__

class sum:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def __add__(self,other):
        return self.a+other.a

    def __repr__(self):
        return f"Hello this is {self.a + self.b}, How are you"
    def __str__(self):
        return f"Hello this is {self.a + self.b+self.c}, How are you"

# obj1 = sum(2,4)
# obj2 = sum(4)
obj3 = sum("naveen","Varshney","Programmer")

print(repr(obj3))
print(str(obj3))
