import csv
fp1=open('data.csv','r')
rows=(csv.reader(fp1))
for row in rows:
    print(row)
    
