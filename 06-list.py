lenguajes=['Python','kotlin','java','javascrip']
print(lenguajes)
#los array (list)cominezan en la posicion 0...
print(lenguajes[0])

#Ordenar los elementos con .sort
lenguajes.sort()
print(lenguajes)

#acceder a un elemento dentro de un texto
aprendiendo =f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificamos valores de un arreglo
lenguajes[2] ='PHP'
print(lenguajes)

#agregar elementos a un arreglo (list)
lenguajes.append ('Ruby')
print(lenguajes)

#eliminar de un arreglo (list)
del lenguajes [1]
print(lenguajes)

#eliminar un arreglo (list)
lenguajes.pop()
print(lenguajes)

#eliminar con pop una posicion especifica
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)
