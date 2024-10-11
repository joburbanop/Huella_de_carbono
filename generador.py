
import random

caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
logitud=int(input("Ingresa tu logitud de contraseña: "))
resultado=''

for  i in range(logitud):
    resultado+=random.choice(caracteres)

print(f"Tu contraseña con longitud {logitud} es: {resultado}")
