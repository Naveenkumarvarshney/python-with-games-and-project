s="My name is khan and my number is {}"
x=s.format(40*60)
print(x)

num = int(input("Enter the number"))
for i in range(1,11):
    # print(f"{num}* {i} = {num*i}")
    # print(format(num)+"*"+format(i)+"="+format(num*i))
    print(num,"*",i,"=",num*i)
