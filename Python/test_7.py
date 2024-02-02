# Dictionary in Python:
d1 = {'apple':50,'mango':100,'guava':200,'banana':500}
print(d1)
print(type(d1))
# Extracting Keys and Values:
# Extracting Keys:
print(d1.keys())
# Extracting Values:
print(d1.values())
# Modifying a Dictionary:
# Adding a new element:
d1 = {'apple':50,'mango':100,'guava':200,'banana':500}
d1['orange'] =5
print(d1)
# Changing an existing element:
d1['banana'] = 80
print(d1)
# Update one dictionary's element with another:
d2 = {'watermelon':1000,'graphs':50,'muskmelon':850}
print(d2)
d1.update(d2)
print(d1)
# Popping an element:
print(d1.pop('banana'))
print(d1)
print(d1.pop('watermelon'))
print(d1)

