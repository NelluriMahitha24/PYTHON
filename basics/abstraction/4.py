from abc import *
class bank(ABC):
    @abstractmethod
    def cal_bal(self):
        pass
class Account(bank):
    min_bal=500
    def __init__(self,id,name,bal):
        self.ID=id
        self.Name=name
        self.Balance=bal
    def cal_bal(self):
        return self.Balance-self.min_bal
a1=Account(101,"Rahul",5000)
print(a1.cal_bal())
        # 4500