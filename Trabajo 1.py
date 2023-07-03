# Define una variable de cada tipo de primitivo
entero = 10
flotante = 3.14
cadena = "Hola, mundo!"
booleano = True
# oncatena la cadena con las otras variables
resultado = cadena + str(entero) + str(flotante) + str(booleano)

# Límite de los enteros en Python
import sys
entero_maximo = sys.maxsize
entero_minimo = -sys.maxsize - 1
# Los enteros en Python no tienen un límite estricto, pero están limitados por la memoria del sistema.

# Límite de los flotantes en Python
flotante_maximo = sys.float_info.max
flotante_minimo = sys.float_info.min
# Los flotantes en Python tienen límites, que pueden consultarse utilizando sys.float_info.

suma_pares = entero * (entero + 1)
