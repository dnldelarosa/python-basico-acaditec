import os
from .names import get_name
from .passwords import get_passwords
import json




def register():
    primer_nombre = get_name(obligatorio=True)
    print("\n")
    segundo_nombre = get_name(prepend=' segundo')
    print("\n")
    primer_apellido = get_name(es_nombre=False, obligatorio=True)
    print("\n")
    segundo_apellido = get_name(es_nombre=False, prepend=' segundo')
    print("\n")
    usuario = get_name(obligatorio=True, prepend='', append=' de usuario', permitir_numeros = True)
    print("\n")
    path = f'data/users/{usuario}.json'
    Exist = os.path.exists(path)

    if Exist:
        print("Este usuario ya existe, por favor intenta nuevamente.")
        usuario = get_name(obligatorio=True, prepend='', append=' de usuario', permitir_numeros = True)
    print("\n")

    clave = get_passwords()
    with open(f'data/users/{usuario}.json', 'w') as f: 
        json.dump({
            'Primer nombre' : primer_nombre, 
            'Segundo nombre' : segundo_nombre , 
            'Primer apellido' : primer_apellido, 
            'Segundo apellido' : segundo_apellido,  
            'usuario': usuario,  
            'clave': clave
            }, f)
    
    print("\n\nSu usuario fue creado con éxito.\n")
    input("Presione enter para continuar.")






















#nombre = get_name()
#apellido = get_name(es_nombre=False)

#print(f"Bienvenido {nombre} {apellido}.")

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

# os.system('cls')