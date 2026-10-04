#Concatenar strings en Python usando el operador ‘+’
#Como veremos a lo largo de este post, en Python existen varias formas de concatenar 
#dos o más objetos de tipo string. La más sencilla es usar el operador +. 
#Concatenar dos o más strings con el operador + da como resultado un nuevo string.
nombre = 'Juan Marcos'
apellidos = 'Miranda Nina'
nombre_completo = nombre + apellidos
print(nombre_completo)

#Como podemos observar, para concatenar dos cadenas con el operador + simplemente 
# necesitamos dos objetos de tipo string. 
# Estos objetos pueden estar almacenados en memoria 
# (usando una variable como en el ejemplo), ser un literal e incluso 
# ser el valor devuelto por una función.

saludo = 'Hola '
hola = saludo + 'Mundo'
print(hola)

#Como he indicado en el párrafo anterior, para concatenar varios strings en Python 
# necesitamos que todos los elementos sean de este tipo. 
# Si tratamos de concatenar, por ejemplo, un string con un int, 
# el intérprete lanzará un error:

suma = 1 + 2
print(suma)

#res = 'El resultado de 1 + 2 es: ' + suma #Corregir con , 

#Para poder concatenar los valores anteriores tienes que convertir suma a un objeto 
# de tipo string. Para ello puedes usar el método str(), que devuelve una 
# representación de tipo string del objeto que se le pasa como parámetro.

suma = 1 + 2
print(suma)

res = 'El resultado de 1 + 2 es: ' + str(suma)
print(res)

#También es posible concatenar más de dos strings a la vez:
print('Suma: ' + str(1) + ' + 2 = ' + str(1 + 2))



#También es posible concatenar más de dos strings a la vez:
print('Suma: ' + str(1) + ' + 2 = ' + str(1 + 2))