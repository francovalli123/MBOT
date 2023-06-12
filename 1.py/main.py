#Main

from base import *
import time

def escribir_letra_por_letra(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.04)
    print()


def deletrear_input(texto, nueva_linea=True):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.04)
    if nueva_linea:
        print()


time.sleep(0.5)
escribir_letra_por_letra("Bienvenido a MBOT.")
time.sleep(0.5)


try:
    solicitud_nickname = "Introduzca su nombre: "
    deletrear_input(solicitud_nickname, nueva_linea=False)
    nickname = input("")
    time.sleep(0.2)
    solicitud_edad = "Introduzca su edad: "
    deletrear_input(solicitud_edad, nueva_linea=False)
    age = int(input(""))
    time.sleep(0.5)
    if len(nickname) == 0:
        escribir_letra_por_letra("Introduzca un nombre de usuario válido.")
        exit()

except ValueError:
    escribir_letra_por_letra("Introduzca una edad válida...")
    exit()


user = MBOT(nickname, age)
print(user.saludo())

def menu():
    escribir_letra_por_letra(f"""{nickname}, ¿En que puedo ayudarte?
                  1- Hablar sobre mi estado actual.
                  2- Consultar que me está pasando.
                  3- Hablar de problemas de autoestima y confianza.
        """)
    
    time.sleep(0.3)

    solicitud_respuesta_menu = "Eliga la opción deseada: "
    deletrear_input(solicitud_respuesta_menu, nueva_linea=False)
    respuesta = int(input(""))

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
    escribir_letra_por_letra("""Que desea hacer?
            1- Salir.
            2- Volver al menú.
            """)
    
    time.sleep(0.3)

    solicitud_respuesta_volver = "Respuesta: "
    deletrear_input(solicitud_respuesta_volver, nueva_linea=False)
    rta = int(input(""))

    time.sleep(0.3)
    if rta == 1:
        escribir_letra_por_letra("Saliendo...")
        time.sleep(0.2)
        exit()
    elif rta == 2:
        menu()
    else:
        escribir_letra_por_letra(f"{nickname}, introduzca '1' para salir del sistema o '2' para volver al menú")
        return ""
        
print(menu())




