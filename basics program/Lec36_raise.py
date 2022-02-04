c = input("Enter your name")
try:
    print(2/0)
    

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")