#   Operadores aritméticos
#================================================
print(" "); titulo = "Operadores aritméticos"; print(titulo)
print("================================================")
#
#Los operadores aritméticos en Python son:
contador = 0; total = 0; porc = 0; valor = 0
contador += 1  # es equivalente a contador = contador + 1
porc = 5  # asigna número entero a variable
total *= porc / 100  # es equivalente a total = total * porc/100
valor = -5  # el signo “-” también se usa para los nº negativos

#   Operadores binarios
#================================================
print(" "); titulo = "Operadores binarios"; print(titulo)
print("================================================")
#
##	Los operadores binarios emplean en sus operaciones 
#	la representación binaria de los datos. Los operadores binarios son:

operacion1 = 1 | 2  # 01 + 10 = 11 → 3 en decimal
operacion2 = 1 & 2  # 01 * 10 = 00 → 0 en decimal
operacion3 = operacion1 ^ operacion2  # 11 * 11 = 11 → 3 

#   Operadores de comparación o relacionales
#================================================
print(" "); titulo = "Operadores de comparación o relacionales"; print(titulo)
print("================================================")
#
##  Los operadores de comparación en Python son:
x = 0; y = 3; z = 4
if y < x == z:  # si 'y' es menor que 'x' y 'x' es igual a 'z'
    print('Se han cumplido las dos condiciones')   
else:
    print('No se han cumplido las dos condiciones')   

#   Operadores lógicos
#================================================
print(" "); titulo = "Operadores lógicos"; print(titulo)
print("================================================")
#
# Anidando operadores con paréntesis “()”.

if (y and not x) or z:
    print('se ha cumplido alguna de las condiciones')