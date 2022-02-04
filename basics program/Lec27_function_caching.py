import time
import datetime
from functools import lru_cache

f=int(input("Enter the size"))
@lru_cache(maxsize=f)
def function(n):
    time.sleep(n)
    return n


print("hello how are you")
function(1)
function(2)
function(3)
print("MY name is naveen")
function(3)
print("smarty")
function(10)
print("holder")


# ---------this is naveen style method--------
# x= datetime.datetime.now()
# print(x.strftime("%A"))


