from poly import *
class one:
    def cal_tax(self):
        print("one class")
class two:
    def cal_tax(self):
         print("two class")
class three:
    def cal_tax(self):
         print("three class")
def execute(obj):
    obj.cal_tax()
execute(one())
execute(two())
execute(three())
    
