print("hello")

list= ['Mango','Orange','kiwi','gauava']
print(list)

# Change in the list
list[1:3]=["watermelon",'banana']
print(list)

# traversing in list
# 1
for x in list:
    print(x)
# 2
for x in range(len(list)):
    print(list[x])

# list comphrension
newlist=[x if x!="banana" else "orange" for x in list]
newlist=[ x  for x in list if x!="banana" ]

     

