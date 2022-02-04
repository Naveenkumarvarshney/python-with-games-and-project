dict = {"mom":"mother","bhai":"brother","mai":"mami"}
input= input("Enter the word you want meaning : ")

for x ,y in dict.items():
    if input in x:
        print(y)