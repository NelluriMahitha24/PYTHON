enames=('Rahul','Sonia','Priyanka','Modi','Amith','Rajni')
#index   0         1         2         3    4       5
new_names=sorted(enames)
print(new_names)
# ['Amith', 'Modi', 'Priyanka', 'Rahul', 'Rajni', 'Sonia']
print(type(new_names))
# <class 'list'>
enames=tuple(new_names)
print(enames)
('Amith', 'Modi', 'Priyanka', 'Rahul', 'Rajni', 'Sonia')
print(type(enames))
# <class 'tuple'>

enames=('Rahul','Sonia','Priyanka','Modi','Amith','Rajni')
#index   0         1         2         3    4       5
enames.sort()
print(enames)
# AttributeError: 'tuple' object has no attribute 'sort'