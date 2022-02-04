print("Enter the no of raw you want")
n = int(input())
print("Enter the two number 1 or 0 only")
num=int(input())

num1=bool(num)

if(num1==True):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
elif(num1==False):
    for i in range(0,n):
        for j in range(n-i,0,-1):
           print("* ",end="")
        print("\r")
else:
    print("You enter wrong input") 


