class One():
    __hello=50
    def sum(self):
       print("I am in in one class")

    def average():
       __B=40

class two(One):
    __A2=40
    def sum(self):
        super().sum()
        print("I am in two")

A= One()
B=two()

print(B.sum())
# ---------------------Method to print private variable_-------------------- 
print(A._One__hello)
print(B._two__A2)