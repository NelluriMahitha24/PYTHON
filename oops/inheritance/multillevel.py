class grand:
    def m1(self):
        print("grand parent class m1 method")
class parent(grand):
    def m2(self):
        print("parent class m2 method")
class child(parent):
    def m3(self):
        print("child class m3 method")
c=child()
p=parent()
c.m1()
c.m2()
c.m3()
p.m1()
p.m2()
# grand parent class m1 method
# parent class m2 method
# child class m3 method
# grand parent class m1 method
# parent class m2 method