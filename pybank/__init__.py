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
    1.11 - Guardar un archivo JSON con toda la información del cliente en la carpeta 'data/users'
"""

import os
from string import punctuation
from .usuario import register


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.system("cls")

def start(error = False):
    os.chdir(dname)
    opcion = input(f"""\n\n    Bienvenido a PyBank\n\n

    Ingrese la opción deseada

    1. Iniciar sesión
    2. Registrarse
    3. Salir

    {"Por favor seleccione 1, 2, o 3, según qué acción desee realizar." if error else ''}

    > """)

    try:
        opcion = int(opcion)
    except:
        os.system('cls')
        # print("""
        # ======================================
        # Por favor Introduzca un número entero.
        # ======================================
        # """)
        return start(True)

    if opcion not in [1, 2, 3]:
        os.system('cls')
        # print("Introdusca un numero ya establecido ")
        return start(True)
    
    if opcion == 2:
        os.system('cls')
        print("\nPara iniciar el registro, favor de ingresar los datos que se le solicite a continuacion.\n")
        register()
        os.system('cls')
        return start()
    elif opcion == 1:
        print("Yes")
    
    

