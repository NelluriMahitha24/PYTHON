class Employee:
    loc="B101"

e1=Employee()
e2=Employee()
e3=Employee()
print(e1)
print(e2)
print(e3)
print(id(e1))
print(id(e2))
print(id(e3))
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)
print(Employee.__dict__)

# <__main__.Employee object at 0x000001C516760740>
# <__main__.Employee object at 0x000001C516760770>
# <__main__.Employee object at 0x000001C5167607D0>
# 1945997018944
# 1945997018992
# 1945997019088
# {}
# {}
# {}
# {'__module__': '__main__', 'loc': 'B101', '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
