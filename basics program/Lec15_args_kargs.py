# def name(list,*tuple):
#     print(list ,tuple)

# name("naveen","harry","naveen","tushar","praveen")

def name(hello,*list1):
   for x,y in hello.items():
       print(x,y)
   print(list1)

list=["hello","how","are","you"]
tuple=("my","name","is","khan")
dict = {"harry":"bhai","tushar":"bhai"}
name(dict,*list)
