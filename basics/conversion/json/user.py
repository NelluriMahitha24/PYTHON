import json
fp1=open("user.json","r")
user_list=json.load(fp1)
employees=[]
for user in user_list:
    employees.append({'eid':user['id'],
                      'ename':user['name'],
                      'email':user['email']},)
fp2=open('useremp.json','w')
json.dump(employees,fp2)
fp1.close()
fp2.close()