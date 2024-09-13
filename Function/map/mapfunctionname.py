enames=["rahul",'sonia','priya','modi']
def changeCase(name):
    return name.upper()
map_obj=map(changeCase,enames)
new_names=list(map_obj)
print(new_names)