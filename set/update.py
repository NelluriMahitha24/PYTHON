s1={10,20,30,40}
s2={50.60,70,80}
s3={1,2,3,4,5}
s1.update(s2,s3)
print(s1)
# {1, 2, 3, 4, 5, 70, 40, 10, 80, 50.6, 20, 30}
# Update a set with the union of itself and others.
s4={1,2,3,4,5,6}
s4.update("Rahul")
print(s4)
# {1, 2, 3, 4, 5, 6, 'R', 'u', 'a', 'h', 'l'}