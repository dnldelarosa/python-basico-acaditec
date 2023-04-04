from string import punctuation
import os
os.system('cls')

# 1.1


def get_name(
        es_nombre: bool = True,
        prepend: str = ' primer ',
        append: str = '',
        obligatorio: bool = False,
        **kwargs
) -> str:
    """ Permite obtener los nombres o apellidos de una persona.

    Esta función pide al usuario ingresar sus nombres o apellido (según el valor del argumento `es_nombre` y el valor `prepend`) tomando en cuenta las siguientes reglas:

    1. Si `es_nombre`: no puede contener espacios, números o caracteres especiales.
    2. Si no `es_nombre`: no puede contener números o caracteres especiales.

    args:
        `es_nombre` (bool): Indica si la función se está utilizando para obtener el nombre (`True`) o el apellido (`False`) del usuario.
        `prepend` (str): Se utiliza para agregar un texto antes d ela palabra clave "nombre" o "apellido".
        `append` (str): Se utiliza para agregar un texto luego de la palabra clave "nombre" o "apellido".
        `obligatorio` (bool): Indica si el campo se puede dejar vacío.
        `kwargs`: Se utiliza para agregar más parametros dentro de la función.
            -`permitir_numeros` (bool): Se usa para permitir el uso de numeros en el valor ingresado, excepto en el primer caracter.

    returns:
        str: El valor ingresado por el usuario, siempre que se cumplan las reglas. 
    """

    permitir_numeros = kwargs.get('permitir_numeros', False)

    if es_nombre:
        palabra = "nombre"
    else:
        palabra = "apellido"

    valor = input(f"Ingrese su{prepend} {palabra}{append}: \n > ")

    lista_nombre = list(valor)

    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if obligatorio and valor == '':
        print("Este campo es obligatorio.")
        return get_name(es_nombre, prepend, append, obligatorio, permitir_numeros=permitir_numeros)

    if (len(lista_nombre) > 0 and permitir_numeros):
        if (lista_nombre[0] in numeros):
            print(
                f"El {prepend}{palabra}{append} no puede comenzar con un número.")
            return get_name(es_nombre, prepend, append, obligatorio, permitir_numeros=permitir_numeros)

    validacion = validar_numeros_signos(lista_nombre, permitir_numeros)
    if validacion > 0:
        print(f"El {prepend}{palabra}{append} no puede contener caracteres especiales{' ni numeros' if not permitir_numeros else ''}.")
        return get_name(es_nombre, prepend, append, obligatorio, permitir_numeros=permitir_numeros)

    if es_nombre:
        if " " in valor:
            print(f"El {palabra}{append} no puede contener espacios.")
            return get_name(es_nombre, prepend, append, obligatorio, permitir_numeros=permitir_numeros)

    return valor


def validar_numeros_signos(lista_nombre, permitir_numeros):
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    res = 0
    for letra in lista_nombre:
        if letra in punctuation or ((not permitir_numeros) and (letra in numeros)):
            res += 1
    return res
