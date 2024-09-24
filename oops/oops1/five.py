class Account:
    min_bal=500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal = amount
        
    def deposit_amount(self,amount):
        self.acc_bal = self.acc_bal+amount
        
a1=Account(101,"Rahul",5000)
a1.deposit_amount(15)
a1.deposit_amount(15)
a2=Account(102,"Sonia",6000)
a3=Account(103,"Priyanka",7000)
a3.deposit_amount(55)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

# {'acc_id': 101, 'acc_name': 'Rahul', 'acc_bal': 5030}
# {'acc_id': 102, 'acc_name': 'Sonia', 'acc_bal': 6000}
# {'acc_id': 103, 'acc_name': 'Priyanka', 'acc_bal': 7055}