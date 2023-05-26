#Main

from base import *
import time

time.sleep(0.5)
print("Bienvenido a MBOT")
time.sleep(0.5)

try:
    nickname = input("Introduzca su nombre de usuario: ")
    time.sleep(0.2)
    age = int(input("Introduzca su edad: "))
    time.sleep(0.5)
    if len(nickname) == 0:
        print("Introduzca un nombre de usuario válido.")
        exit()

except ValueError:
    print("Introduzca una edad válida...")
    exit()


user = MBOT(nickname, age)
print(user.saludo())

def menu():
    print(f"""{nickname}, ¿En que puedo ayudarte?
                  1- Hablar sobre mi estado actual.
                  2- Consultar que me está pasando.
                  3- Hablar de problemas de autoestima y confianza.
        """)
    
    time.sleep(0.3)

    respuesta = int(input("Eliga la opción deseada: "))

    if respuesta == 1:
        print(user.pregunta_1())
        print(volver())
    elif respuesta == 2: 
        print(user.pregunta_2())
        print(volver())
    elif respuesta == 3:
        print(user.pregunta_3())
        print(volver())


def volver():
    print("""Que desea hacer?
            1- Salir.
            2- Volver al menú.
            """)
    
    time.sleep(0.3)

    rta = int(input("Respuesta: "))

    time.sleep(0.3)
    if rta == 1:
        print("Saliendo...")
        time.sleep(0.2)
        exit()
    elif rta == 2:
        menu()
    else:
        return f"{nickname}, introduzca '1' para salir del sistema o '2' para volver al menú"
        
print(menu())



