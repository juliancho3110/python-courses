names=["Pablo", "Johan", "Pedro"]#variable tipo lista con 3 elementos
for n in names: # n va a tomar en cada interaccion un valor dentro de la variable names
    print(f"name : {n}")
###########################
numbers=[3,6,9,12,15,18]
for a in numbers:
    print(f"number : {a}")
###########################
indices=[0,1,2,3,4,5]
for i in indices:
    print(f"indice :{i}")
###########################
print(names[0])#  el numero dentro de los parentesis cuadrados determinan el indice que quiero leer
print(numbers[4])
print(indices[2])
###########################
j=indices[4]
print(f"indice: {j}")
print(f"numero:{numbers[j]}")
k=0
print(names[k])
############################
i=0
print(f"indice: {i},numero:{numbers[i]}")
i=1
print(f"indice: {i},numero:{numbers[i]}")
i=2
print(f"indice:{i}, numero:{numbers[i]}")
i=3
print(f"indice: {i}, numero:{numbers[i]}")
print()
for i in indices:
    print(f"indice: {i}, numero:{numbers[i]}")