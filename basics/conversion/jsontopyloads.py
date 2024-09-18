import json
emp='''{"id":101,"name":"rahul","Avai":true,"loc":"undefined","sal":null}'''
print(emp)
emp_dict=json.loads(emp)
print(type(emp_dict))
print(emp_dict)