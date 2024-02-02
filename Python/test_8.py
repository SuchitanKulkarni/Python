# Set in Python:
s1 = {1,3.14,'sparta'}
print(s1)
s1 = {1,3.14,'sparta',1,3.14}
print(s1)
# Set Operations:
# Update one dictionary's element with another:
s1 = {1,2,4}
print(s1)
s1.add('money')
print(s1)
# Updating multiple elements:
s1.update([6,8,9,0])
print(s1)
# Removing an element:
s1.remove(9)
print(s1)
# Set Functions:
# Union of two sets:
s1 = {1,2,3,4,5}
s2 = {7,8,9,0,6}
s1 = s1.union(s2)
print(s1)
# Intersection of two sets:
s3 = {4,5,6,7,}
s1 = {1,2,3,4}
print(s1)
print(s3)
s2 = s1.intersection(s3)
print(s2)