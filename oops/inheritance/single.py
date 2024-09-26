class parent:
    def m1(self):
        print("parent class m1 method")
    def m2(self):
        print("parent class m2 method")
class child(parent):
    def m3(self):
        print("child class m3 method")
    def m4(self):
            print("child class m4 method")
c=child()
c.m1()
c.m2()
c.m3()
c.m4()
# parent class m1 method
# parent class m2 method
# child class m3 method
# child class m4 method