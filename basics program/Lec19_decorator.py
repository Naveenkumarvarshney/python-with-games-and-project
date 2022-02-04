# def decorator(func):
#     def inner():
#         func()
#         print("The peogram end")
#     return inner

# @decorator
# def sum():
#     print("I am the sum you fuck off")

# sum()

# def decorator(func):
#     def inner():
#         func()
#         print("The peogram end")
#     return inner

# def sum():
#     print("I am the sum you fuck off")

# func_return= decorator(sum)
# func_return()

def decorator(sum):
    def inner():
        sum()
        print("The peogram end")
    return inner

def sum():
    print("I am the sum you fuck off")

func_return= decorator(sum)
func_return()

