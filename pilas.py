# Crear una pila vacía
pila = []

pila.append(23)
pila.append(100)
pila.append(25)

# for item in pila:
#     print(item)

print('Autilización del contenedor antes del pop')
auxl = pila.pop()
print('Hola {auxl}')

print('Autilización del contenedor despues del pop')
for item in pila:
     print(item)

print('Autilización del contenedor despues del -1')
auxl2 = pila[-1]
print(auxl2)