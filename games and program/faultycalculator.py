from ast import Break


def calculator():
    print("Welcome to naveen calculator")

    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")

    operator =input("Enter the operator")

    print("Enter the numbers")
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))

    if(operator=="+"):
        if(num1==56):
            print(num1,"+",num2,"=", 77)
        else:
            print(num1,"+",num2,"=", num1+num2)
    elif(operator=="-"):
        print(num1,"-",num2,"=", num1-num2)
    elif(operator=="*"):
        print(num1,"*",num2,"=", num1*num2)
    elif(operator=="/"):
        print(num1,"/",num2,"=", num1/num2)
    else:
        print("You choose wrong operator")
    again()

def again():
     choose=input("input 'yes' for gain opertaion otherwise 'no'")
     if(choose=="yes"):
         calculator()
     elif(choose=="no"):
          print("see you later")
          Break
     else:
        again()

calculator()   

