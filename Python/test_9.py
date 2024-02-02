# If Statement:
a = 10
b = 20
if b>a:
    print('B is greater than A')
if a>b:
    print("A is greater than B")
if a>b:
    print('A is greater than B')
else:
    print('B is greater than A')
a = 39
b = 39
if b>a:
    print('B is greater than A')
else:
    print("A is greater than B")
a = 10
b = 20
c = 30
if a>b:
    print('Gold')
elif b>c:
    print('Silver')
else:
    print('platinum')
if (a>b) & (a>c):
    print('A is greater')
elif (b>a) & (b>c):
    print('B is greater')
else:
    print('C is greater')
# If with Tuple:
tup1 = ('a','b','c','d')
print(tup1)
if 'g' in tup1:
    print('Gold')
else:
    print('Diamond')
# If with List:
L1 = [1,2,3,4,5]
print(L1)
if L1[2]==3:
    L1[2]=6
    print(L1)
# If with Dictionary:
D1 = {'k1':15,'k2':47,'k3':70}
print(D1)
if D1['k3']==70:
    D1['k3']= D1['k3']+100
    print(D1)