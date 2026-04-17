#Datos para a usar#
game_name = "empty"
game_ver = 0
game_saveFolder_location = "empty"

#control de bucle#
confirm_info = []

#Comienzo del programa#
print ("GAME DATA MANAGER iniciado: ")
while confirm_info != "S":
    print ("Ingrese el nombre del juego: ")
    game_name = input ()
    
    print ("Ingrese la versión del juego: ")
    game_ver = input ()
    
    #este debe permitirme generar otros espacios de memoria por si hay más de un DLC#
    game_dlcs = []
    while True:
            dlc = input("Ingrese el nombre del DLC (o escriba 'fin' para terminar, 'no tiene' si no hay): ")
            if dlc.lower() == 'fin' or dlc.lower() == 'no tiene':
                    break
            else:
                game_dlcs.append(dlc)

    #En este punto consultar si se quiere añadir otro y repetir la operación#
    
    print ("Ingrese La ruta del save/data del juego: ")
    game_saveFolder_location = input ()
    
    #Mostrar los datos ingresados#
    print ("Los datos cargados son los siguientes: ")
    print (f"Título- {game_name}; Versión operativa- {game_ver}; Ubicación de guardados- {game_saveFolder_location}")
    print(f"DLC(s): {', '.join(game_dlcs) if game_dlcs else 'Ninguno'}")

    #pregunta de control#
    confirm_info = input("\nSon estos datos correctos? (s/n)").upper()
    if confirm_info == "S":
        break
    

#Añadir anotación final#
print("\n¿Desea agregar notas adicionales? (ej: errores de mods, requisitos de hardware, etc.)")
game_notes = input("Notas: ") #preparar esta línea para que gestione textos más largos#

#Pedir confirmación para generar el documento#

#Generar el archivo#

