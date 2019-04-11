
#   Palabras reservadas de Python (30)
#========================================
print(" "); titulo = "Palabras reservadas de Python (30)"; print(titulo)
print("================================================")
#
##	No se pueden declarar variables, objetos, funciones y clases con 
#	estos términos. El siguiente código muestra la lista de palabras reservadas:
#	
#	import keyword
#	print(keyword.kwlist)

"""
and, as, assert, break, class, continue, def, del, elif,
else, except, finally, for, from, global, if, import, in, is,
lambda, nonlocal, not, or, pass, raise, return,
try, while, with, yield 
"""
#	\newline 	Ignored
#	\\ 			Backslash (\)
#	\' 			Single quote (')
#	\" 			Double quote (")
#	\a 			ASCII Bell (BEL)
#	\b 			ASCII Backspace (BS)
#	\f 			ASCII Formfeed (FF)
#	\n 			ASCII Linefeed (LF)
#	\r 			ASCII Carriage Return (CR)
#	\t 			ASCII Horizontal Tab (TAB)
#	\v 			ASCII Vertical Tab (VT)
#	\ooo 		ASCII character with octal value ooo
#	\xhh... 	ASCII character with hex value hh...


#   Declarar Variables
#==============================================
print(" "); titulo = " Declarar Variables"; print(titulo)
print("================================================")
#
##	El signo igual “=” se utiliza para asignar números, booleanos, 
#	cadenas y expresiones a las variables de un programa.

numero_entero = 5  # declara variable numérica
Numero_Entero = 5  # declara otra variable numérica distinta
x = y = z = 5  # asignación múltiple: x=5, y=5 y z=5
m, n = 5, 4 * 8  # asignación múltiple: m = 5 y n = 32
p1, p2 = (1, 2)  # asignación múltiple de tupla: p1 = 1 y p2 = 2 
cadena = 'Python3'  # declara cadena alfanumérica
cadena = 'Pytonisos\tdel\tmundo\n'  # incluye tab y salto de línea
cadena = '''cadenas
            que ocupan
            varias líneas'''  # declara cadena de varias líneas'
numero_float1 = 23.45  # números con decimales 
numero_float2 = 0.1e-3  # números con notación científica
numero_hexadecimal = 0x23  # número hexadecimal
booleano_verdad = True  # booleano: Verdadero
booleano_falso = False  # booleano: Falso
booleano_negar = not booleano_falso  # True, Verdadero
numero_complejo = 2 + 4j * 2  # (2+8j)

cadena1 = "4.5" # declara cadena1
cadena2 = "67" # declara cadena2
numero1 = float(cadena1) # Convierte cadena a flotante -> 4.5
numero2 = int(cadena2) # Convierte de cadena a entero -> 67

var_nula = None  # Declara variable con valor vacío o nulo 


#   Asignar múltiples valores de una lista
#==============================================
print(" "); titulo = "Asignar múltiples valores de una lista"; print(titulo)
print("================================================")
#
a, *b = [1, 2, 3, 4]  # a toma primer valor y b lista con los demás
print('a', a)  # 1
print('b', b)  # [2, 3, 4]

#   Cadenas crudas: raw
#==============================================
print(" "); titulo = "Cadenas crudas: raw"; print(titulo)
print("================================================")
##	Cualquier cadena que deba interpretarse tal como 
#   se escribe es una cadena raw o cruda.

##	En una cadena raw se omiten los caracteres especiales 
#   expresados con la barra invertida “\”.

##	Las cadenas raw se escriben entrecomilladas y con el 
#   carácter “r” precediéndolas:

print('\\5', ' es igual que ', r'\5')


#   Operaciones básicas con variables
#==============================================
print(" "); titulo = "Operaciones básicas con variables"; print(titulo)
print("================================================")

##	Varias variables que contienen cadenas pueden unirse (concatenarse) 
#	con el signo más “+”. También, dos o más cadenas pueden unirse expresándolas 
#	entrecomilladas, una a continuación de la otra. Es más, cualquier cadena 
#	puede replicarse un número de veces con el operador “*”.
	
##	Con la función type() podemos conocer el tipo de datos de una variable 
#	y con la sentencia del borramos una variable de memoria. Una vez borrada
# 	si intentamos acceder a su valor se producirá un error.

##	Los métodos upper() y lower() devuelven una cadena en mayúsculas 
#	y minúsculas, respectivamente.

##	En las expresiones matemáticas es posible establecer la prioridad 
#	en la resolución de las operaciones mediante el uso de paréntesis.

cadena1 = 'Python'  # Declara cadena con 'Python'
cadena2 = 'Lenguaje ' + cadena1.upper()  # Lenguaje PYTHON
cadena3 = 'Lenguaje ' 'Python'  # Lenguaje Python
cadena3 = cadena1.lower() * 3  # pythonpythonpython 
cadena4 = "Python para impacientes"
print(cadena4.title())  # Python Para Impacientes 

# Uso de paréntesis en expresiones
total1 = ((24 - 10 + 2.3) * 4.3 / 2.1) ** 2
print(total1)  # 1113.9700907
print(type(cadena1))  # type str=""
print(type(total1))  # type float=""
del cadena1  # Borra la variable de memoria
#print(cadena1)  # Genera un error porque no existe

#   Las funciones ord() y chr()
#===================================================
print(" "); titulo = "Las funciones ord() y chr()"; print(titulo)
print("================================================")

##  La función ord() devuelve el ordinal entero del 
#   carácter indicado y justo lo contrario hace la 
#   función chr() que devuelve el carácter (Unicode) 
#   que representa al número indicado.

ord('$')  # 36
ord('@')  # 64
ord('A')  # 65
ord('ñ')  # 241
ord('Ұ')  # 1200
ord('€')  # 8364
ord('娼')  # 23100

chr(36)  # '$'
chr(64)  # '@'
chr(65)  # 'A'
chr(241)  # 'ñ'
chr(1200)  # 'Ұ'
chr(8364)  # '€'
chr(23100)  # '娼'

#   Métodos para evaluar cadenas
#================================================
print(" "); titulo = "Métodos para evaluar cadenas"; print(titulo)
print("================================================")

##	cadena.isalpha()
#	Devuelve verdadero (True) si todos los caracteres en la 
#   cadena son alfabéticos.
#	
##	cadena.isalnum()
#	Devuelve verdadero (True) si todos los caracteres en la 
#   cadena son alfanuméricos.
#	
##	cadena.isdecimal(), cadena.isdigit(), cadena.isnumeric()
#	Devuelve verdadero (True) si todos los caracteres en la 
#   cadena son números.
#	
##	cadena.isspace()
#	Devuelve verdadero (True) si todos los caracteres son 
#   espacios en blanco.
#	
##	cadena.islower(), cadena.isupper()
#	Devuelve verdadero (True) si todos los caracteres son 
#   minúsculas o mayúsculas, respectivamente.
#	
##	cadena.istitle()
#	Devuelve verdadero (True) si el primer carácter de la 
#   cadena es mayúsculas y el resto minúsculas; o en el 
#   caso de que haya palabras separadas por espacios en 
#	blanco que cumplan la misma regla.

cadena1 = "Cuba"
cadena2 = "Costa Rica"
print(cadena1.isalpha())   # True
print(cadena1.isalnum())   # True
print(cadena1.isdecimal())   # False
print(cadena1.isspace())   # False
print(cadena2.istitle())   # True
if cadena1.isalpha():
    print("Todos los caracteres que contiene son alfabéticos")

