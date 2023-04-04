import os
from names import get_name
from getpass import getpass

def login():

    usuario = get_name(obligatorio=True, prepend='', append=' de usuario', permitir_numeros = True)
    print("\n")
    clave = getpass("Ingrese su contraseña")
    path = f'data/users/{usuario}.json'
    Exist = os.path.exists(path)

    if Exist:
        print(f"Bienvenido {usuario}.")

login()
