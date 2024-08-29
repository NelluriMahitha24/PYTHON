emp = {
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45,
    'avail':True
}

for x in emp.keys():
    print(x)
# Dict_Name.keys() -> a set-like object providing a view on Dict_Name's keys
# eid
# ename
# esal
# avail
for y in emp.values():
    print(y)
# Dict_Name.values() -> an object providing a view on Dict_Name's values
# 101
# Rahul
# 45000.45
# True

for a,b in emp.items():
    print(a,b)
# Dict_Name.items() -> a set-like object providing a view on Dict_Name items
# eid 101
# ename Rahul
# esal 45000.45
# avail True