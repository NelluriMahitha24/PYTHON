class Test:
    def __init__(self):
        self.a = 100
    def m1(self):
        self.b=200


t1=Test()
t2=Test()
t1.m1()
t2.c=300
print(t1.__dict__)  #{'a': 100, 'b': 200}
print(t2.__dict__)  #{'a': 100, 'c': 300}