
#   Control del flujo: if
#================================================
titulo = "Control del flujo: if"; print(titulo)
print("================================================")
#
##	La sentencia if se utiliza para controlar el flujo en 
#   la ejecución de un programa. 
##	Básicamente, si se cumple una condición puede hacerse 
#   que se ejecute un bloque de código, que estará sangrado, 
#   y si no se cumple o se dan otras posibilidades puede 
#	hacerse que se ejecuten otros bloques, igualmente sangrados. 
##	Para ello, se apoya en las clausulas elif que evalúa otras 
#   condiciones y en else, que en caso de no cumplirse ninguna 
#   de las condiciones anteriores ofrece la solución final.


# Evaluar distintos valores numéricos
edad = 10; precio = 0
if edad <= 12:  # se evalúa la primera condición... 
    precio = 2  # y si edad es menor igual que 12, precio = 2
elif 13 <= edad <= 18:  # en caso contrario se evalúa...
    precio = 3  # si edad está entre 13 y 18, precio = 3
else:  # en cualquier otro caso...
    precio = 4  # precio = 4

#print( 'A Pagar: ' + str(precio) ) 
print('A Pagar: ' + str(precio) + ' Euros')  # Muestra importe

# Evaluar en una sola línea

print('par' if edad % 2 == 0 else 'impar')  

# Evaluar si un valor está entre varios posibles

tecla = 'S'
if tecla in('s', 'S', 'y', 'Y'):
    print('Ha seleccionado: Sí')

# Evaluar variables booleanas

respuesta = True
if respuesta:  # Evalúa si respuesta es True
    print('Sí, es verdad')
else:
    print('Es falso')

# Evaluar variables por tipo de dato que contienen

var1 = "Python 3 para impacientes"
var2 = 3
var3 = 3.14
var4 = True
var5 = [1, 2, 3]
var6 = ('a', 'b', 'c')
var7 = {'a':1, 'b':2, 'c':3}

if type(var1) is str:
    print("'var1' es una cadena")

if type(var2) is int:
    print("'var2' es una número entero")

if type(var3) is float:
    print("'var3' es un número con decimales")

if type(var4) is bool:
    print("'var4' es un booleano")

if type(var4):
    print("'var4' es un booleano")

if type(var5) is list:
    print("'var5' es una lista")

if type(var6) is tuple:
    print("'var6' es una tupla")

if type(var7) is dict:
    print("'var7' es un diccionario")

# Evaluar si cadena, lista o diccionario están vacíos

var1 = ""
var2 = []
var3 = {}

if not var1:
    print("Cadena vacía")

if not var2:
    print("Lista sin elementos")
    
if not var3:
    print("Diccionario sin claves/valores")

# Evaluar si una variable no tiene ningún valor

var4 = None
if not var4:
    print("No tiene ningún valor")



#   Control del flujo con bucles: while
#================================================
print(" "); titulo = "Control del flujo con bucles: while"; print(titulo)
print("================================================")
#
##	El bucle más elemental suele emplearse cuando un 
#	programa necesita repetir un número de veces un proceso 
#	hasta que una variable alcanza un valor o hasta que 
#	se cumple alguna condición predeterminada. Por ello, 
#	en muchos casos, los bucles incorporan variables que 
#	actúan como contadores que van cambiando su valor en 
#	cada ciclo o variables que representan un cambio de 
#	estado (p.e. verdadero y falso). 

##	La sentencia while incluye la condición que debe 
#	cumplirse para que se ejecute el bloque de código que 
#	contiene, aunque en cualquier momento podemos salir 
#	de un bucle con break o cancelar el ciclo actual y 
#	continuar con continue la ejecución del ciclo siguiente.
#

# Ejemplo de bucle con 'break'
print('Ejemplo de bucle con \"break\"')    
contador = 0
limite = 5
while contador < 11:  # el bucle termina cuando contador=10 
    if contador == limite:  # o cuando alcance el valor limite 
        break
    else:
        contador += 1  # contador se incrementa en 1
        print(contador, limite)

print("")

# Ejemplo de bucle con 'continue' y 'break'
print('Ejemplo de bucle con \"continue\" y \"break\"')    
x = 0
y = 0
limite = 5
while True:
    y += 1
    if y != limite:
        x += y
    else:
        break
    if y != 3:
        continue    
    print(x, y)

##	En un bucle infinito
print('Ejemplo de bucle Infinito')    
##	En un bucle infinito en el lugar de una condición se 
#	escribirá True o el valor 1. Las instrucciones del bucle 
#	se ejecutarán indefinidamente hasta que se fuerce su fin 
#	con un break.  

contador = 0
while True:
    contador += 1
    if contador == 10:  # cuando valor de contador sea 10...
        break  #  ...terminará la ejecución del bucle


#   Control del flujo con bucles: for...in
#================================================
print(" "); titulo = "Control del flujo con bucles: for...in"; print(titulo)
print("================================================")
#
##	 Otra forma de construir un bucle consiste en 
#	recorrer los elementos de un lista con la sentencia 
#	for...in. 
#
##	La construcción utiliza una variable que 
#	en cada ciclo toma el valor de un nuevo elemento 
#	de la lista de la clausula in. 
#	
##	El bucle terminará cuando se alcance el último 
#	elemento de la lista o cuando se fuerce su 
#	fin con break. 

loteria = [12019, 23023, 90326, 40506, 89450, 21023, 13237]
for numero in loteria:
    if numero == 21023:
        print('Tiene el primer premio:', numero) 
        break


##	Ejemplo de bucle bucles: for...in range()
print(""); print('Ejemplo de bucle bucles: for...in range()')    
##	Con for también se puede usar la clausula in range 
#	que, en su uso más elemental, recorre una secuencia 
#	de valores (ver más opciones).

for num in range(10):
    print(num)  # recorre del 0 al 9