import json
# import csv
emp_dict=[{'id': 101, 'name': 'rahul', 'Avai': True, 'loc': 'undefined', 'sal': None},
          {'id': 102, 'name': 'rajeev', 'Avai': False, 'loc': 'undefined', 'sal': None}]
fp=open('pytojsons.json','w')
# fp1=open("data.csv","w")
json.dump(emp_dict,fp)
# print(type(data))
# print(data)
# print(len(data))
fp.close()
