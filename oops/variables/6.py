class Test:
    def __init__(self):
        self.a = 100


t1=Test()
t2=Test()

print(t1.__dict__)  #{'a': 100}
print(t2.__dict__)  #{'a': 100}