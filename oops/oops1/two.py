class Test:
    def __init__(self):
        print("Test Class - Constructor method")
    def m1(self):
        print("Test class - Instance Method")
    @classmethod
    def m2(cls):
        print("Test class - class method")
    @staticmethod
    def m3():
        print("Test Class - static method")

t1=Test()
t2=Test()
t1.m1()
t1.m1()
t1.m1()
t1.m1()
t1.m1()
t1.m1()

# Test Class - Constructor method
# Test Class - Constructor method
# Test class - Instance Method
# Test class - Instance Method
# Test class - Instance Method
# Test class - Instance Method
# Test class - Instance Method
# Test class - Instance Method