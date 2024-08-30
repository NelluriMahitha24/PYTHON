emp={'id':101,'name':'mahi','sal':550000}
value=emp.setdefault('fname','nelluri')
print(value)
print(emp)

# nelluri
# {'id': 101, 'name': 'mahi', 'sal': 550000, 'fname': 'nelluri'}