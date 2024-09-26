class Employee:
    company_name="TCS"
    def __init__(self,id,name,sal):
        #create instance variables  - self
        self.eid=id
        self.ename=name
        self.esal = sal


e1=Employee(101,"Rahul",45000)
e2=Employee(102,"Sonia",55000)
e3=Employee(103,"Priyanka",65000)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)

# {'eid': 101, 'ename': 'Rahul', 'esal': 45000}
# {'eid': 102, 'ename': 'Sonia', 'esal': 55000}
# {'eid': 103, 'ename': 'Priyanka', 'esal': 65000}