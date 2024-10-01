from abc import *
class bank(ABC):
    @abstractmethod
    def cal_tax(self):
        pass
b=bank()
print(b)
print(id(b))