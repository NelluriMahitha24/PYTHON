import csv
fp1=open('data.csv','r')
rows=list(csv.reader(fp1))
for row in rows:
    print(row)