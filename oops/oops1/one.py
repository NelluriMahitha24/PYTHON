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

Test()

# Test Class - Constructor method