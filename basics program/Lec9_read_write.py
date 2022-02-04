# f= open("Naveen.txt","r")

# 1 : Method  to read a file
# content=f.read()
# print(content)

# 2 : Method  to read a file
# for line in f:
#     print(line,end="")

# f= open("Naveen2.txt","w")
# f.write("naveen ke bat hi alaag h")

f= open("Naveen3.txt","a")
f.write("hello how are you")
# f.write("hello how are you naveen")
# f.write("hello how are you tinku")
f.close()

f=open("Naveen3.txt","r")
content=f.read()
f.seek(2)
print(content)

# f=open("Naveen2.txt","r+")
# content=f.read()
# print(content)
# # f.write("Hello how are you")
# # f.seek(10)
# # print(f.read())
# # ***print a list form***
# print(f.readlines())              
# f.close()




