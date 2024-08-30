emp1={'id':101,'name':'mahi','sal':550000}
emp2={'id':102,'name':'mahitha','sal':650000}
emp1.update({'avail':True})
emp1.update(emp2)
print(emp1)
print(emp2)
# {'id': 101, 'name': 'mahi', 'sal': 550000, 'avail': True}