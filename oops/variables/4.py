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
print(Employee.__dict__)

# {'__module__': '__main__', 'company_name': 'TCS', '__init__': <function Employee.__init__ at 0x000001FE7C79D1C0>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
