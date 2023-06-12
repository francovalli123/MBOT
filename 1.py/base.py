#MBOT
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

class MBOT:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    
    def __str__(self):
        escribir_letra_por_letra(f"Tu nombre es {self.name} y tenes {self.age} años.")
        return ""
    
    def saludo(self):
        escribir_letra_por_letra(f"\n¡Hola {self.name}! Mi nombre es MBOT y estoy aca para ayudarte.\n")
        return ""
    
        
    def pregunta_1(self):
        escribir_letra_por_letra(f"Contame {self.name}, ¿Como estuvo tu día?\n")
        time.sleep(0.2)
        escribir_letra_por_letra("""Selecciona tu respuesta:
                 1- Bien.
                 2- Mas o menos.
                 3- Mal.        
            """)
        time.sleep(0.1)
        solicitud_respuesta_p1_1 = "Respuesta: "
        deletrear_input(solicitud_respuesta_p1_1, nueva_linea=False)
        day_info = int(input(""))
        if day_info == 1:
            time.sleep(0.2)
            escribir_letra_por_letra(f"\nMe alegro de oír eso {self.name}. ¿Que te ha gustado de tu día?\n")
            time.sleep(0.3)
            solicitud_respuesta_p1_2 = "Respuesta: "
            deletrear_input(solicitud_respuesta_p1_2, nueva_linea=False)
            day_info_2 = input("")
            time.sleep(0.2)
            if len(day_info_2) == 0:
                escribir_letra_por_letra("Por favor, introduzca una respuesta.")
                return ""
            else:
                escribir_letra_por_letra(f"\n¡Que bueno {self.name}! Recuerda que la clave para superar momentos dificiles es poder ver las solo las cosas buenas de cada día.\n")
                return ""
            
        elif day_info == 2:
            time.sleep(0.2)
            escribir_letra_por_letra(f"Lamento eso {self.name}, ¿Que te ha disgustado?\n")
            time.sleep(0.3)
            solicitud_respuesta_p1_3 ="Respuesta: "
            deletrear_input(solicitud_respuesta_p1_3, nueva_linea=False)
            day_info_3 = input("")
            time.sleep(0.2)
            if len(day_info_3) == 0:
                escribir_letra_por_letra("Por favor, introduzca una respuesta.")
                return ""
            else:
                escribir_letra_por_letra("\n¿Y que pensas acerca de eso?\n")
                time.sleep(0.3)
                solicitud_respuesta_p1_4 = "Respuesta: "
                deletrear_input(solicitud_respuesta_p1_4, nueva_linea=False)
                reply_day_info_3 = input("")
                time.sleep(0.2)
                if len(reply_day_info_3) == 0:
                    escribir_letra_por_letra("Por favor, introduzca una respuesta.")
                    return ""
                else:
                    escribir_letra_por_letra(f"\nPensá en las cosas buenas que pasaron hoy {self.name}, no siempre todo va a salir como lo previsto. Mañana será un nuevo día y debes superar esas cosas que pasaron hoy para mejorar lo de hoy.\n")
                    return ""
        elif day_info ==  3:
            time.sleep(0.2)
            escribir_letra_por_letra(f"\nLamento mucho eso {self.name}, te daré tu espacio para que puedas desahogarte.\n")
            time.sleep(0.3)
            solicitud_respuesta_p1_5 = "Cuentame todo: "
            deletrear_input(solicitud_respuesta_p1_5, nueva_linea=False)
            day_info_4 = input("")
            if len(day_info_4) == 0:
                escribir_letra_por_letra("Por favor, introduzca una respuesta.")
                return ""
            else:
                time.sleep(0.2)
                escribir_letra_por_letra(f"\nLa vida es así {self.name}, ¿Cómo te sentís en este momento acerca de lo ocurrido?\n ")
                time.sleep(0.3)
                solicitud_respuesta_p1_6 = "Respuesta: "
                deletrear_input(solicitud_respuesta_p1_6, nueva_linea=False)
                reply_day_info_4 = input("")
                if len(reply_day_info_4) == 0:
                    escribir_letra_por_letra(f"Por favor {self.name}, estoy acá para ayudarte. Podés contarme.")
                    return ""
                else:
                    if self.age >= 11 and self.age <= 20:
                        escribir_letra_por_letra(f"\n{self.name}, estás pasando por una etapa de tu vida donde es normal sentirse mal y no decirle a nadie. No te preocupes, estoy acá para ayudarte.\n")
                    else:
                        escribir_letra_por_letra(f"\n{self.name} recordá que a veces la vida puede ser dificíl y aunque sea un simple bot, el sentido de mi vida es ayudarte. A continuación te voy a hacer un par de preguntas.\n")
                    time.sleep(0.2)
                    escribir_letra_por_letra("""¿Puedes hacer algo para mejorar lo que pasó?
                             1- Si
                             2- No\n""")
                    time.sleep(0.3)
                    solicitud_respuesta_p1_7 = "Respuesta: "
                    r_1_1 = int(input(""))
                    if r_1_1 == 1:
                        escribir_letra_por_letra (f"""\nEntonces no te pongas mal, el problema eventualmente será resuelto. Pensá en que a veces nos preocupamos demasiado por cosas que no valen tanto la pena.\nY siempre va a haber gente para escucharte, e incluso si no lo hay, acá estoy yo.\nMañana va a ser un nuevo día, y aunque parezca no significar nada, serán 24 horas mas para poder resolver tus problemas y sentirte mucho mejor.\nEs normal tener un día malo, incluso pueden ser meses o años, pero nunca hay que bajar los brazos sobre todo sabiendo que tiene solución.\nSomos los protagonistas de nuestra propia vida, y nadie va a venir a jugar ese papel por nosotros, no bajes los brazos.\n
                        """)
                        time.sleep(0.2)
                        escribir_letra_por_letra("¿Que puedes hacer al respecto?")
                        time.sleep(0.3)
                        solicitud_respuesta_p1_8 = "Respuesta: "
                        deletrear_input(solicitud_respuesta_p1_8, nueva_linea=False)
                        r_1_1_2 = input("")
                        if len(r_1_1_2) == 0:
                            escribir_letra_por_letra("Necesito que pienses en algo para poder ayudarte.")
                        else:
                            escribir_letra_por_letra(f"Ahora ya sabes que tenés que hacer {self.name}, incluso si fallas, intentalo una y otra vez hasta que puedas solucionarlo.\n")
                            return ""

                    elif r_1_1 == 2:
                        escribir_letra_por_letra(f"""Entonces no deberías preocuparte por algo sin solución. Buscá cosas que te hagan sentir bien y olvidarte de lo que está pasando.\nRecuerda que sobrepensando tanto algo vas a crear problemas que ni siquiera existen y te sentirás peor.\nPiensa en como mejorar tu vida y dejar de lado todo eso que te hace mal, y si es como en este caso en el que no puedes encontrar una solución al problema, deja de preocuparte tanto y recuerda que no estas solo. Siempre va a haber alguien para acompañarte y escucharte.\n""")
                        return ""
                    else: 
                        escribir_letra_por_letra(f"{self.name}, elige una opción válida.")
                        return ""
        else:
            escribir_letra_por_letra(f"{self.name}, elige una opción válida.")
            return ""

    def pregunta_2(self):
        escribir_letra_por_letra("Has elegido la opción para saber que puedes estar sufriendo (Elige solo 6).")
        time.sleep(0.5)
        escribir_letra_por_letra(""" ¿Cuales de los siguientes sintomas padeces?\n 
                  
                  1- Sensación de nerviosismo, agitación o tensión.\n
                  2- Sensación de peligro inminente, pánico o catástrofe.\n
                  3- Problemas para concentrarse o para pensar en otra cosa que no sea la preocupación actual.\n
                  4- Tener problemas para conciliar el sueño.\n
                  5- Estado de ánimo irritable o bajo la mayoría de las veces.\n
                  6- Cambio grande en el apetito, a menudo con aumento o pérdida de peso.\n
                  7- Cansancio y falta de energía.\n
                  8- Sentimientos de inutilidad, odio a sí mismo y culpa.\n
                  9- Miedo a la contaminación o a la suciedad. \n
                  10- Necesidad de tener las cosas ordenadas y simétricas.\n
                  11- Pensamientos agresivos u horribles sobre la pérdida de control y el daño a sí mismo o a otros.\n
                  12- Pensamientos no deseados, incluida la agresión, o temas sexuales o religiosos.\n
        """)
        respuesta_2_1 = []
        time.sleep(0.5)
        while len(respuesta_2_1) < 6:
            solicitud_respuesta_p2 = "Introduzca la opción deseada: "
            deletrear_input(solicitud_respuesta_p2, nueva_linea=False)
            respuesta = int(input(""))
            respuesta_2_1.append(respuesta)

            solicitud_respuesta_p2_salir = "¿Ha terminado de elegir? S/N: "
            deletrear_input(solicitud_respuesta_p2_salir, nueva_linea=False)
            salir = input("").upper()
            if salir == "S":
                break
            elif salir == "N":
                continue
            else:
                escribir_letra_por_letra("Por favor, ingresa un 'S' si ha terminado de elegir opciones y una 'N' si desea continuar.")

        time.sleep(0.5)

        if respuesta_2_1.count(1) + respuesta_2_1.count(2) + respuesta_2_1.count(3) + respuesta_2_1.count(4) >= 3:
            escribir_letra_por_letra("De acuerdo con las opciones elegidas, lamento informarte que padeces de Ansiedad, te recomiendo buscar ayuda profesional para una solución más efectiva.\nNo obstante, yo puedo ayudarte un poco.")
            return ""
        elif respuesta_2_1.count(5) + respuesta_2_1.count(6) + respuesta_2_1.count(7) + respuesta_2_1.count(8) >= 3:
            escribir_letra_por_letra("De acuerdo con las opciones elegidas, lamento informarte que padeces de Depresión, te recomiendo buscar ayuda profesional para una solución más efectiva.\nNo obstante, yo puedo ayudarte un poco.")
            return ""
        elif respuesta_2_1.count(9) + respuesta_2_1.count(10) + respuesta_2_1.count(11) + respuesta_2_1.count(12) >= 3:
            escribir_letra_por_letra("De acuerdo con las opciones elegidas, lamento informarte que padeces de Transtorno Obsesivo Compulsivo(TOC), te recomiendo buscar ayuda profesional para una solución más efectiva.\nNo obstante, yo puedo ayudarte un poco.")
            return ""
        else:
            escribir_letra_por_letra(f"Lamento informarte que mi base de datos no pudo identificar el transtorno. ¿Puede ser que no hayas encontrado alguna opción que se adapte a tu situación?\n")
            time.sleep(0.2)
            solicitud_respuesta_p2_2 = "S/N: "
            deletrear_input(solicitud_respuesta_p2_2, nueva_linea=False)
            r_2_2 = input("\n").casefold()
            if r_2_2 == "N":
                escribir_letra_por_letra("Lo lamento, aún estoy en desarrollo.\n")
                return ""
            elif r_2_2 == "S":
                escribir_letra_por_letra("Entonces, vuelve a intentarlo.\n")
                return ""
            else:
                escribir_letra_por_letra("Por favor, proporcione una respuesta válida.\n")
                return
            
    def pregunta_3(self):
        print("Has elegido la opción para hablar de problemas de confianza y autoestima.\n")
        time.sleep(0.2)
        print("""A continuación te voy a mostrar una serie de sintomas, necesito que elijas un maximo de 5 que te identifiquen.\n
                 
                 1- Inseguridad.
                 2- No aceptar ningún tipo de crítica.
                 3- Defenderse incluso cuando nadie ataca.
                 4- Incapacidad para hacer la propia voluntad.
                 5- Incapacidad de relacionarse con personas del sexo opuesto.  
        """)

        time.sleep(0.2)
        respuesta_3_1 = []
        time.sleep(0.5)
        while len(respuesta_3_1) < 5:
            respuesta = int(input("Introduzca la opción deseada: "))
            respuesta_3_1.append(respuesta)

            salir = input("¿Ha terminado de elegir? S/N: ").upper()
            if salir == "S":
                break
            elif salir == "N":
                continue
            else:
                print("Por favor, ingresa un 'S' si ha terminado de elegir opciones y una 'N' si desea continuar.\n")
        
        time.sleep(0.5)

        if respuesta_3_1.count(1) + respuesta_3_1.count(2) + respuesta_3_1.count(3) + respuesta_3_1.count(4) + respuesta_3_1.count(5) >= 3:
            print(f"{self.name}, lamento informarte que posiblemente padezcas de baja autoestima y poca confianza.\n A continuación vamos a intentar solucionar eso.\n La clave para superar esto es tener confianza en ti mismo. Te daré tips para conseguirla.\n1- Construye una actitud de confianza mental.\n2- Se bondadoso con vos mismo cuando te compares con los demás.\n3- Desprendete de las dudas sobre vos mismo.\n4- Corre riesgos seguros.\n5- Reconoce tu talento y dejá que brille. ")
            return f"Ahora {self.name} debes comprometerte a seguir estos consejos para salir de esta situación. Valdrá la pena. Igualmente te recomiendo contactar a un profesional humano."
        else:
            return f"Entonces no tienes estos problemas, ¡felicidades {self.name}!"
    
    
