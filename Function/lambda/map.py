def add(mark):
    return mark+1
marks=[10,20,30,40]
object=map(add,marks)
print(object)
print(type(object))
print(list(object))
