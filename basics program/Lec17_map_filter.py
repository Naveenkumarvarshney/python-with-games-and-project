# list=["50","60","70"]

# for i in range(len(list)):
#     list[i]=int(list[i])

# list[0]=list[0]+2
# print(list)


# listname=["50","60","70"]
# num=list(map(int,listname))
# print(num)

# listname=[50,60,70]
# num =list(map(lambda x:x*x,listname))
# print(num)

def square(a):
    return a*a

function =[square]
for i in range(5):
    num=list(map(lambda x:x(i),function))
    print(num)

# listname=[10,3,4,5,6,7]
# num=list(map(square,listname))
# print(num)


# ---------------------#filterfunction#---------------------#
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
  
  
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
  
# using filter function
# filtered = list(map(fun, sequence))
filtered=filter(fun,sequence)
  
print('The filtered letters are:')
for s in filtered:
    print(s)