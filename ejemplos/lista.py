import sys 
""" lista=[8,4,6,8,6,7,5,0,4,5]

print(sys.getsizeof(lista)) """
listas=[]
for i in range(40):
    listas.append(i)
    print(sys.getsizeof(listas))


