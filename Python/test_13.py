# Lambda (Anonymous Function) :
g = lambda x:x*x*x
print(g(7))
print(g(10))
print(g(45))
# Lambda Functions :
# Lambda with filter:
L1 = [12,3,4,56,87,34,90,54]
final_list = list(filter(lambda x:x%4!=0,L1))
print(final_list)
# Lambda with Map:
L1 = [2,3,4,5,6,7,9]
final_list = list(map(lambda x:x*5,L1))
print(final_list)
# Lambda with Reduce:
# by submodule:
from functools import reduce
L1 = [1,2,3,4,5,6,8]
final_list = (reduce(lambda x,y:x+y,L1))
print(final_list)


