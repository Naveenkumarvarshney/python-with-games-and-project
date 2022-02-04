
# -------this is the all the method created by Naveen(The coder)-------
# Method 1: 
# list =[30,40,60]
# for i in range (len(list)):
#      print(list[i])

# Method 2:
# list =[30,40,60]
# myit=iter(list)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# Method 3:
# list =[30,40,60]
# myit= list.__iter__()

# print(myit.__next__())
# print(myit.__next__())
# print(myit.__next__())

# Method 4: Using genertor-generator is used to iterate by one only
# ------creating generator-----

def looping(n):
    for i in range(n):
        #------ this is generator declartion usig yield---------
        # yield value ko hold karke rakhta h
        yield i     
    
myit=looping(5)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


