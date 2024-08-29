l1=[1,2,3,4,5]
l2=[]
l2=l1.copy()
print(l1)
print(l2)
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
print(id(l1))
print(id(l2))
# 2130758932736
# 2130759236800
# Return a shallow copy of the list.