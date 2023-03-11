# Proyecto PyBank
"""
Estamos trabajando en un proyecto para crear el sistema de un banco.


Funcionalidades:

1- Crear un menú de opciones para el usuario:
    1.1- El menú debe tener las siguientes opciones:
        1.1.1- Crear un nuevo cliente
        1.1.2- Crear una nueva cuenta
        1.1.3- Depositar dinero
        1.1.4- Retirar dinero
        1.1.5- Transferir dinero
        1.1.6- Mostrar información de una cuenta
        1.1.7- Mostrar información de un cliente
        1.1.8- Editar información de un cliente
        1.1.9- Eliminar una cuenta
        1.1.10- Eliminar un cliente

1- Crear un nuevo cliente: 
    1.1- Se le pedirá al usuario que ingrese el nombre, apellido, sexo, edad, 
        altura, si está casado y si tienes hijos.
    1.2- Cuando se solicita la información al cliente se le debe dar opciones 
        válidas para que el usuario pueda ingresar la información correctamente. 
        El sistema no debe dar errores.
    1.3- Las palabras como Bienvenido/Bienvenida Señor/Señora deben ser asignados 
        automáticamente según el sexo del cliente.
    1.4 - El primer nombre y primer apellido, no pueden contener números o 
        caracteres especiales.
    1.5 - El sexo debe ser M o F.
    1.6 - La edad debe ser un número entero y mayor a 0. 
        Si la persona es menor de 18 años, no se le permitirá crear la cuenta, 
        y se detiene el proceso.
    1.7 - La altura debe ser un número decimal y mayor a 0.
    1.8 - Casado e Hijos deben ser S o N.
    1.9 - Solicitar nombre de usuario
    1.10 - Solicitar contraseña
"""

import os
from string import punctuation

os.system("cls")


print("\n\nBienvenido a PyBank\n\n")


# 1- Crear un nuevo cliente:
# 1.1


def get_name(es_nombre=True):
    if es_nombre:
        palabra = "nombre"
    else:
        palabra = "apellido"
    nombre = input(f"Ingrese su primer {palabra}: \n > ")
    lista_nombre = list(nombre)
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    res = 0
    for letra in lista_nombre:
        if letra in punctuation or letra in numeros:
            res += 1
    if res > 0:
        print(f"El {palabra} no puede contener caracteres especiales o números.")
        return get_name()
    if es_nombre:
        if " " in nombre:
            print("El nombre no puede contener espacios.")
            return get_name()
    return nombre


nombre = get_name()
apellido = get_name(es_nombre=False)

print(f"Bienvenido {nombre} {apellido}.")

sexo = input("Sexo: (M/F) \n > ")
estado_civil = input(f"¿Está usted casad{'o' if sexo.lower() == 'm' else 'a'}? \n > ")

# nombre = primer_nombre()

# def primer_apellido():

#     caracteres_especiales = ["@", "/", "-", "+"]
#     numeros = [0,1,2,3,4,5,6,7,8,9]

#     apellido = input("Ingrese su apellido: ")

#     if nombre in caracteres_especiales or numeros:
#         print("Nombre ingresado correctamente.")
#     else:
#         print("Tu nombre contiene caracteres especiales o numeros, intenta nuevamente.")
#         return primer_apellido()


# nombre = primer_apellido()


# #nombre_apellido()

# def get_sexo():
#     sexo = input("Ingrese su sexo (M/F): ")
#     if sexo.lower() in ["m", "f"]:
#         return sexo
#     else:
#         print("Sexo no válido")
#         return get_sexo()

# sexo = get_sexo()


# def pedirNumeroEntero():
#     correcto = False
#     num = 0
#     while (not correcto):
#         try:
#             num = int(input("\nIntroduzca su Edad: >"))
#             if num == 0 or num >= 18:
#                 correcto = True
#             else:
#                 print("NO tienes la mayoria de Edad: No cumples con los Requisitos.")
#         except ValueError:
#             print("ERROR, introduce un numero Entero: ")
#     return num

# edad = pedirNumeroEntero()

# def altura():
#     altura = float(input("Ingrese su estatura:"))
#     if altura == float:
#         return altura()

# altura = altura()

# def get_casado():
#     casado = int(input("Ingresa 0 si eres Soltero o 1 si eres Casado segun tu estado civil: "))
#     if casado.lower() in ["m", "f"]:
#         return casado
#     else:
#         int(input("Ingresa 0 si eres Soltera o 1 si eres Casada segun tu estado civil: "))
#         return get_casado()

# if sexo.lower() in ["m"]:
#     int(input("Ingresa 0 si eres Soltero o 1 si eres Casado segun tu estado civil: "))
# else:
#     int(input("Ingresa 0 si eres Soltera o 1 si eres Casada segun tu estado civil: "))

# #casado =

# hijos = int(input("Ingresa 0 si tienes hijos o 1 si no tienes hijos: "))

# print(f"Bienvenid{'a' if sexo.lower() == 'f' else 'o'} a la familia PyBank, Señor{'a' if sexo.lower() == 'f' else ''} {primer_apellido}")

# input("Presione ENTER para salir...")
