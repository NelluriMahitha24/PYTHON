class m1:
    def me1(self):
        print("m1 class me1 method")
class m2(m1):
    def me2(self):
        print("m2 class me2 method")
class m3(m1):
    def me3(self):
        print("m3 class me3 method")
class m4(m1):
    def me4(self):
        print("m4 class me4 method")
obj1=m1()
obj2=m2()
obj3=m3()
obj4=m4()


obj1.me1()
obj2.me1()
obj2.me2()
obj3.me1()
obj3.me3()
obj4.me1()
obj4.me4()

# m1 class me1 method
# m1 class me1 method
# m2 class me2 method
# m1 class me1 method
# m3 class me3 method
# m1 class me1 method
# m4 class me4 method
