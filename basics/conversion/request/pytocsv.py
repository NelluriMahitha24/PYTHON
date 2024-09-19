import csv
emp_dict=[{'id': 101, 'name': 'rahul', 'Avai': True, 'loc': 'undefined', 'sal': None},
          {'id': 102, 'name': 'rajeev', 'Avai': False, 'loc': 'undefined', 'sal': None}]
fp1=open('pytocsv.csv','w')
wr=csv.writer(fp1)
wr.writerow(['id','name','Avai','loc','sal'])
for emp in emp_dict:
    wr.writerow([emp['id'],emp['name'],emp['Avai'],emp['loc'],emp['sal']])