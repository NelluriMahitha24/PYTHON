import json
emp_dict={'id': 101, 'name': 'rahul', 'Avai': True, 'loc': 'undefined', 'sal': None}
print(emp_dict)
emp_json=json.dumps(emp_dict)
print(type(emp_json))
print(emp_json)