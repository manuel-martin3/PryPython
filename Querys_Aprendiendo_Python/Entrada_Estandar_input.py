#   Entrada Estándar: input()
#================================================
print(); titulo = "Entrada Estándar: input()"; print(titulo)
print("================================================")
#
##	La función input() permite a los usuarios introducir 
#	datos de distintos tipos desde la entrada estándar 
#	normalmente se corresponde con la entrada de un teclado). 

#   Introducir datos de distinto tipo
#================================================
print(); titulo = "Introducir datos de distinto tipo"; print(titulo)
print("================================================")
#

edad = int(input('Teclear edad: '))  # entrada de entero
peso = float(input('Teclear peso: '))  # entrada de flotante
nombre = input('Teclear nombre: ')  # entrada de cadena
print(nombre, edad, 'años', peso, 'kg')  # muestra datos


#   Introducir datos con captura de errores (excepciones)
#================================================
print(); titulo = "Introducir datos con captura de errores (excepciones)"; print(titulo)
print("================================================")
#

try:  # bloque de código a comprobar
    articulos = int(input('Artículos:'))  # entrada de un número 
    precio = int(input('Precio:'))  # entrada de un número
    print('Pagar: ' + str(articulos*precio) + ' Euros') # muestra resultado

except:  # bloque para captura de error
    print('error, deben ser números')  # muestra mensaje


#   Introducir datos con captura de errores en bucle
#================================================
print(); titulo = "Introducir datos con captura de errores en bucle"; print(titulo)
print("================================================")
#
##	En el siguiente ejemplo si se produce un error no se detendrá el proceso. 
##	Volverá a pedirse que se introduzca un dato numérico gracias al bucle.
#
tramos = 0
total = 0
while True:
    try:
        distancia = int(input('Distancia: '))
        if distancia == 0:
            break
        else:
            tramos += 1
            total += distancia
            print('Los {} tramos miden {} km.'.format(tramos,total))
    except:
        print('Debes teclear un número entero')


#   Introducir fechas y horas con captura de errores
#================================================
print(); titulo = "Introducir fechas y horas con captura de errores"; print(titulo)
print("================================================")
#
        
##	Para validar la entrada de fechas y horas se utiliza la 
#	función strptime() del módulo datetime que convierte la 
#	entrada introducida a un tipo de datos llamado datetime. 

##	En caso de que no pueda convertirla porque no se adecue 
#	a una fecha/hora correcta producirá una excepción.
        

import datetime

while True:
    try:
        fecha = input("Introducir Fecha dd-mm-aaaa: ")
        fecha = datetime.datetime.strptime(fecha, "%d-%m-%Y")
        break
 
    except:
        print ("Fecha incorrecta\n")

print(fecha)    

