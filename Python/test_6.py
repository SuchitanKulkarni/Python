# List in Python:
L1 = [1, 'sparta',3.14,True]
print(L1)
print(type(L1))
# Extracting Individual Elements:
print(L1[0])
print(L1[-1])
print(L1[1:3])
# Modifying a List:
# Changing the element at 0th index:
print(L1)
L1[0]=100
print(L1)
#Appending a new element:
L1.append(-87.99)
print(L1)
# Popping the last element:
L1.pop()
print(L1)
# Reversing elements of a List:
L1 = ['434',12,90,True,False]
print(L1)
L1.reverse()
print(L1)
# Inserting element at a specified index:
L1.insert(3,'hello')
print(L1)
# Sorting a List:
L1 = ['a','f','d','b','z']
L1.sort()
print(L1)
# Concatenating List:
L1 = [1,2,3,4,5]
L2 = [8,9,0,7,6]
print(L1+L2)
# Repeating elements:
print(L1*8+L2)
