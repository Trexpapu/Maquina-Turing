#============================================================
#                     FUNCIONES 
#============================================================

#Ejemplo 
#(q0 a q0 a der)
#(q0 b q0 b der)
#(q0 B qh B izq)

#-------------------------------------------------------
#                     VALIDAR CADENA 
#-------------------------------------------------------
def validarCadena():
    print("Validar Cadena")
    
    cadena = input("Ingrese una cadena: ")
    
    estado_actual = 'q0'  # Establece el estado inicial
    cabezal = 0
    simbolos = []
    mensaje = ""
    for i in cadena:
        simbolos.append(i)
    print(simbolos)
    while True:
        transicion = estados_transiciones.get(estado_actual, False)
        print(transicion)
        print(estado_actual)
        if estado_actual == "qh":
            print("Cadena valida")
            mensaje = "Cadena valida"
            break
        elif transicion == False:
            print("Cadena invalida, no existe transición")
            mensaje = "Cadena invalida, no existe transición"
            break
        else:
            bandera = False
            for sublista in transicion:
                if 0 >= cabezal < len(simbolos):
                    pass 
                else:
                    simbolos[cabezal] = "B"
                if simbolos[cabezal] == sublista[0]:
                    estado_actual = sublista[1]
                    simbolos[cabezal] = sublista[2]
                    if sublista[3] == "der":
                        cabezal += 1
                    else:
                        cabezal -= 1
                    bandera = True
                    break
            if bandera == False:
                mensaje = "Cadena invalida"
                print("Cadena invalida")
                break
    with open('historial.txt', 'a') as archivo:
        archivo.write(f'Cadena = {cadena} {mensaje}-----De la MT {ruta}\n')





       



#-------------------------------------------------------
#                     LEER MAQUINA 
#-------------------------------------------------------
def cambiarMaquina():
    print("Cambiar Maquina")

    # Ruta del archivo
    global ruta
    ruta = input("Ingresa la ruta del archivo: ")  

    #Intentar abrir el archivo 
    try: 
        # Abrir el archivo 
         with open(ruta, "r") as archivo:
            for line in archivo:#recorre cada linea del archivo
                # Verificar si la línea del archivo está vacía o en blanco y omitirla si es el caso
                if not line.strip():
                    continue
                
                # elimina paréntesis y saltos de línea, y luego divide la línea
                # en palabras usando espacios como separadores, almacenando estos
                # datos procesados en la variable contenido.
                contenido = line.strip('()\n').split()
                maquina_turing.append(contenido)

            # Imprimir la lista de transiciones
            print(maquina_turing)

            # Obtener los valores en la lista y meterlos a variables
            for transicion in maquina_turing:#recorrer la lista usando ciclo for   
                print(transicion)         
                # Extraer los valores de la transición
                estado_actual = transicion[0]       #Accedemos a la posicion 0 de la lista
                simbolo_leido = transicion[1]       #Accedemos a la posicion 1 de la lista
                estado_siguiente = transicion[2]    #Accedemos a la posicion 2 de la lista
                simbolo_escrito = transicion[3]     #Accedemos a la posicion 3 de la lista
                direccion = transicion[4]           #Accedemos a la posicion 4 de la lista


                #meter clave valor al diccionario
                if estado_actual in estados_transiciones: #si la clave ya existe añadimos informacion
                                                              # a la clave en otras palabras si un estado tiene
                                                              #  mas transiciones
                    estados_transiciones[estado_actual].append([simbolo_leido, estado_siguiente, simbolo_escrito, direccion])
                else:#si el estado solo tiene una transicion creamos la clave-valor
                    estados_transiciones[estado_actual] = [[simbolo_leido, estado_siguiente, simbolo_escrito, direccion]]

    except FileNotFoundError:
        print("Ruta no encontrada")








#-------------------------------------------------------
#                     HISTORIAL CADENAS 
#-------------------------------------------------------
def historialCadenas():
    #editar el archivo de texto y agregar la cadena y su resultado asi
    #Cadena = Cadena invalida/valida
    print("Historial de Cadenas")
    try:
        with open ("historial.txt", "r") as archivo:
            contenido = archivo.read()

        print(contenido)    
    except FileNotFoundError:
        print("No existe el archivo")







#============================================================





#============================================================
#                     MENU 
#============================================================

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("        MAQUINA DE TURING          ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Integrantes:")
print("Carlos ")
print("Emmanuel ")
print("Melba ")
print("Scarlett ")
print("-----------------------------------\n")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("         MENU PRINCIPAL          ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
print("Opciones:")
print("1. Validar Cadena")
print("2. Cambiar Maquina")
print("3. Historial de Cadenas ")
print("4. Salir")

maquina_turing = []	#lista donde guardaremos los datos del archivo
estados_transiciones = {} #diccionario en donde vamos a guardar toda la informacion de los estados y transiciones

while True:
    opcion = input("\nSelecciona una opción: ")

    if opcion == '1':
        validarCadena()
    elif opcion == '2':
        maquina_turing.clear()
        estados_transiciones.clear()
        cambiarMaquina()
        print(estados_transiciones) # print de prueba imprime el diccionario
    elif opcion == '3':
        historialCadenas()
    elif opcion == '4':
        print("Autodestrución en 3... 2... 1...")
        print("\n-----------------------------------\n")
        break
    else:
        input(
            "Opción no válida")

#============================================================
