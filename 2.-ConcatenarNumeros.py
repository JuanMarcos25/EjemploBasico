#Para concatenar dos números en Python, podemos hacer dos cosas diferentes:

#Si queremos concatenar 2 y 3, el resultado será 23, así que podemos, 
#como primera opción, convertir estos números a string, 
#concatenarlos como strings con el operador "+" y posteriormente convertirlos a enteros de nuevo:
a = 2
b = 3
print(a+b)

c =str(a) + str(b)
print(c) #Cadena es el resultado "23"

print(int(str(a) + str(b))) #El resultado es un numero 23