def function1():
    x=100
    def function2():
        global x
        x=500
        
        print("hhello",x)
        print("hdfjhdkfhhello",x)
    function2()
    print("function1",x)


