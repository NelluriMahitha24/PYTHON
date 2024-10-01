from abc import *
class bank(ABC):
    def cal_tax(self):
        pass
b=bank()
print(b)
print(id(b))