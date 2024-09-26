class m1:
    def me1(self):
        print("m1 class me1 method")
class m2:
     def me2(self):
            print("m2 class me2 method")
class m3(m1,m2):
     def me3(self):
            print("m3 class me3 method")
c=m3()
c.me1()
c.me2()
c.me3()
# m1 class me1 method
# m2 class me2 method
# m3 class me3 method
    