# Data Structures in Python:
# Tuple in Python:
tup1 = (1,True,3.14,5-4j)
print(tup1)
print(type(tup1))
# Extracting Individual Element:
tup1 = (1,True,3.14,5-4j)
print(tup1[0])
print(tup1[-1])
print(tup1[0:2])
# Tuple Basic Operations:
# Finding Length of Tuple:
print(len(tup1))
# Concatenating Tuple:
tup1 = (1,2,3)
tup2 =(3,4,5)
print(tup1+tup2)
print(tup2+tup1)
# Repeating Tuple Elements:
tup1 = (1,2,3)
print(tup1*5)
# Repeating and Concatenating:
print(tup1*4+tup2)
# Minimum Value:
tup1 = (20,78,90,45)
print(min(tup1))
# Maximum Value:
print(max(tup1))