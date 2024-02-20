#Vamos hacer un generador de contraseñas con letras, números y signos
#1. Vamos a importal los modulos. Usaremos random y string

import random, string

#Ahoramos vamos a crear una función
def generar_contrasena(n): #n es el número de caracteres
    caracteres = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    contrasena = []
    
#ahora vamos a hacer un bucle para que se repita n veces    
    for i in range(n):
        tmp = random.choice(caracteres)
        contrasena.append(tmp)
        res = ''.join(contrasena)
    return res

n = int(input('Ingresa el número de caracteres: '))
test = generar_contrasena(n)
print(test)

#auqnue funciona, no es la mejor forma de hacerlo. Vamos a hacerlo de otra forma
#por tema de seguridad es mejor usar secrets en vez de random ya que es más seguro. ya que random es predecible 
#ya que random son pseudoaleatorios, lo que significa que son deterministas y reproducibles y se conoce el estado interno de nuestro generador.
#secrets es más seguro porque usa un generador de números aleatorios criptográficamente seguro, que es mucho más difícil de predecir..

#import secrets, string



#def generar_contrasena(n): #n es el número de caracteres
#    caracteres = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
#    contrasena = []
    
 
#    for i in range(n):
#        tmp = secrets.choice(caracteres)
#        contrasena.append(tmp)
#        res = ''.join(contrasena)
#    return res


#n = int(input('Ingresa el número de caracteres: '))
#test = generar_contrasena(n)
#print(test)