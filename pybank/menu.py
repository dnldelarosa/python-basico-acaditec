import os
from string import punctuation

os.system("cls")

# 1- Crear un menú de opciones para el usuario

def get_menu(apellido: str, sexo: int, error = 0):
    opcion = input(f"""\n\nBienvenid{'o' if sexo == 1 else 'a'} {'Sr.' if sexo == 1 else 'Sra.'} {apellido}\n\n

    Ingrese la opción deseada

    1. Crear una nueva cuenta
    2. Depositar dinero
    3. Retirar dinero
    4. Transferir dinero
    5. Mostrar información de una cuenta
    6. Mostrar información de un cliente
    7. Editar información de un cliente
    8. Eliminar una cuenta
    9. Eliminar un cliente

    {"Por favor Introduzca un número entero." if error == 1 else ''}
    {"Introdusca un numero ya establecido." if error == 2 else ''}

    >""")
    try:
        opcion = int(opcion)
    except:
        os.system('cls')
        # print("""
        # ======================================
        # Por favor Introduzca un número entero.
        # ======================================
        # """)
        return get_menu(1)

    if opcion not in range(1, 10):
        os.system('cls')
        # print("Introdusca un numero ya establecido ")
        return get_menu(2)

    #return opcion
