from getpass import getpass
import base64

def get_passwords():


    password = getpass("Introduzca una contraseña: ")
    if password == '':
        print("Su contrseña no puede estar vacia.")
        return get_passwords()
    validar_passwords = getpass("Introduzca su contrseña nuevamente: ")
    if password == validar_passwords:
        clave = password
        clave_encriptada = clave.encode('utf-8')
        base64_bytes = base64.b64encode(clave_encriptada)
        base64_clave = base64_bytes.decode('utf-8')
        
        return base64_clave
    else:
        print("Las contraseñas no coinciden. Intente nuevamente por favor.")
        return get_passwords()
    

