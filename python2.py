import random

def generar_contraseña(longitud):
    contraseña = ""
    for i in range(longitud):
        contraseña += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789" + "!#$%&'()*+,-./:;<=>?@[\]^_{|}~")
    return contraseña

longitud = 8
print(generar_contraseña(longitud))