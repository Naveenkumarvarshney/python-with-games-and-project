# Operator	Magic Method
# +	__add__(self, other)
# –	__sub__(self, other)
# *	__mul__(self, other)
# /	__truediv__(self, other)
# //	__floordiv__(self, other)
# %	__mod__(self, other)
# **	__pow__(self, other)
# >>	__rshift__(self, other)
# <<	__lshift__(self, other)
# &	__and__(self, other)
# |	__or__(self, other)
# ^	__xor__(self, other)


# Operator	Magic Method
# <	__LT__(SELF, OTHER)
# >	__GT__(SELF, OTHER)
# <=	__LE__(SELF, OTHER)
# >=	__GE__(SELF, OTHER)
# ==	__EQ__(SELF, OTHER)
# !=	__NE__(SELF, OTHER)

class sum:
    def __init__(self,a):
        self.a=a
    
    def __add__(self,other):
        return self.a+other.a

obj1 = sum(2)
obj2 = sum(4)
obj3 = sum("naveen ")
obj4 = sum("varshney")

print(obj1+obj2)
print(obj3+obj4)
