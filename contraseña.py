import random
import string

def generar_contrasenia(longitud):
    
    caracteres = string.ascii_letters + string.digits
    contrasenia = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasenia
longitud_contrasenia = 6  
contrasenia_aleatoria = generar_contrasenia(longitud_contrasenia)
print(contrasenia_aleatoria)
                