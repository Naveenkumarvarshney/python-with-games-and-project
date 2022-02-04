import pickle

list = ["banana","Apple",'Pineaplle',"guava"]
file=open("hello.txt","wb")
text=pickle.dump(list,file)
file.close()

fileobj=open("hello.txt","rb")
obj=pickle.load(fileobj)
print(obj)




# important Notes:
# pickle.load() - takes file object and return corresponding python format (readable ) 
# pickle.loads() - takes the binary format and returns python format
# pickle.dumps() - takes the variable and returns binary string


