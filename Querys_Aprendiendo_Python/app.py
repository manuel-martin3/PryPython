

print("   ")
print("1° parte Formateo basado en %, en str.format() y string.Template() ")
print("##################################################################")

# Iniciando con saludos
print("hola mundo")

# Asignacion de valores
x = 1
print(x + 3)

# El formato basado en % sólo es válido para los tipos de 
# datos str, int y float:
nombre = 'Martin'
edad = 30
altura = 1.70
print('%s tiene %i años y mide %f metros' %(nombre,edad,altura))

# Aplica formatos numéricos ajustando la precisión:
valor1 = 8.56767
valor2 = 9.45548
print('1° valor = {0:.3} y 2° valor = {1:.4}'.format(valor1, valor2))

# Alinea y rellena con caracteres:
for alin, txt in zip('<^>', ['izquierda', 'centro', 'derecha']):
    print('{0:{fill}{align}30}'.format(txt, 
          fill="*", 
          align=alin))

# Rellena con guiones bajos:
print('{0:_^30}'.format('Python para impacientes'))

# Tiene el inconveniente de la falta de concisión cuando
# se insertan valores en una cadena:
vel = 120
print('Velocidad permitida: {vel} Km/h.'.format(vel=vel))

# Incluso en su forma abreviada es algo enrevesado:
print('Velocidad permitida: {} Km/h.'.format(vel))


# Formateo con string.Template
# ----------------------------
# Con string.Template también se pueden insertar los 
# valores de variables y/o expresiones en una cadena,
# aunque la brevedad brilla por su ausencia:
from string import Template
import datetime

perfi = Template('$nom es $pro con un salario de $sal e.')
print(perfi.substitute(
    nom = 'Martin',
    pro = 'Analista',
    sal = 1200
))

fecha = datetime.date(2018, 3, 11)
contrato = Template('Su contrato se hizo el $dia')
print(contrato.substitute(dia=fecha))


# Operadores Aritmeticos 
y = 4; print("El valor [=] asignado para (y) es : {0}".format(y))
z = 3; print("El valor [=] asignado para (z) es : {0}".format(z))
y = 4; z = 3; y+=z; print("1° forma La suma [+=] es : {0}".format(y))
y = 4; z = 3; print("2° forma La suma [+] es: {0}".format(y + z))
y = 4; z = 3; y-=z; print("1° forma La resta [-=] es : {0}".format(y))
y = 4; z = 3; print("2° forma La resta [-] es: {0}".format(y - z))
y = 4; z = 3; y*=z; print("1° forma El producto [*=] es : {0}".format(y))
y = 4; z = 3; print("2° forma El producto [*] es: {0}".format(y * z))
y = 4; z = 3; y/=z; print("1° forma El division [/=] es : {0}".format(y))
y = 4; z = 3; print("2° forma La division [/] es: {0}".format(y / z))
y = 4; z = 3; print("El resto [%] es: {0}".format(y % z))
y = 4; z = 3; print("La igualdad [==] es: {0}".format(y == z))
y = 4; z = 3; print("La desigualdad [!=][<>] es: {0}".format(y != z))
y = 4; z = 3; print("El valor es mayor [>] ?: {0}".format(y > z))
y = 4; z = 3; print("El valor es menor [<] ?: {0}".format(y < z))
y = 4; z = 3; print("El valor es mayor igual [>=] ?: {0}".format(y >= z))
y = 4; z = 3; print("El valor es menor igual [<=]?: {0}".format(y <= z))
y = 4; z = 3; print("1° forma redondeo hacia abajo [//] es: {0}".format(y // z))
y = 4; z = 3; y//=z; print("2° forma redondeo hacia abajo [//] es: {0}".format(y))
y = 4; z = 3; print("1° forma potenciacion [**] es : {0}".format(y ** z))
y = 4; z = 3; y**=z; print("2° forma potenciacion [**] es : {0}".format(y))

print("   ")
print("2°  Las cadenas de formato f ")
print("###############################")

x = 0; y = 3; z = 5

if(x==y):
    print("El valor {0} y {1} son iguales".format(z, y))
else:
    print("El valor {0} y {1} no son iguales".format(z, y))


if(x == y > z):
    print("El valor {0} es igual a {1} y es mayor a {2} ".format(x, y, z))
else:
    print("El valor {0} no es igual a {1} y no es mayor a {2} ".format(x, y, z))


total = 0
valor = 0
numeros = [1,2,3,4,5,6,7,8,9]
for valor in numeros:
    total+= valor
    print('{0}° valor de la lista y el acumulado es {1}'.format(valor, total))

