import opcode
import os
from tkinter import ARC

game_name = "empty"
game_ver = 0
game_saveFolder_location = "empty"
game_notes = "empty"
nombre_archivo_sav = "empty"
game_dlcs = []
yesNote = ""
confirm_save = []
confirm_info = []

create_read_delete = ""

def generador_archivos(nombre_docuSave, nombreJuego, versionJuego, dlcsJuego, rutaSaves, notasDeJugador):
    try:
        #añade el .txt al final#
        if not nombre_docuSave.endswith(".txt"):
            nombre_docuSave += ".txt"
           
        with open(nombre_docuSave, "w", encoding="utf-8") as f:
            f.write (f"Título: {nombreJuego}\n")
            f.write (f"Versión: {versionJuego}\n")
            f.write (f"DLC(s): {dlcsJuego}\n")
            f.write (f"Ruta de partidas guardadas: {rutaSaves}\n")
            f.write (f"Notas del usuario: {notasDeJugador}\n")
            f.write (f"-" *30 + "\n")
            print(f"Archivo creado en: {os.getcwd()}\\{nombre_docuSave}\n")
    except PermissionError:
        print("error inesperado")
        return game_name, game_ver, game_dlcs, game_saveFolder_location, game_notes

#limpieza de datos en consola#
def limpiar_pantalla():
    print("\033[H\033[J", end="")

def solicitud_datos():
    #control de bucle#
    confirm_info = []
    print ("GAME DATA MANAGER iniciado: ")
    while confirm_info != "S":
        game_dlcs = []
        print ("Ingrese el nombre del juego: ")
        game_name = input ()

        print ("Ingrese la versión del juego: ")
        game_ver = input ()

        while True:
                dlc = input("Ingrese el nombre del DLC (o escriba 'fin' para terminar, 'no tiene' si no hay): ")
                if dlc.lower() == 'fin' or dlc.lower() == 'no tiene':
                        break
                else:
                    game_dlcs.append(dlc)
    
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
    return game_name, game_ver, game_dlcs, game_saveFolder_location

def nota_final():
    yesNote = input("\n¿Desea agregar notas adicionales? (ej: errores de mods, requisitos de hardware, etc.) --S/N--").upper()
    if yesNote == "S":
        game_notes = input("Notas: ")
        return game_notes

def confirmar_generar_documento():
    confirm_save = input("Desea generar un archivo .txt con la información?:...(S - generar archivo/N - salir sin guardar) \n").upper()
    if confirm_save == "S":
        nombre_archivo_sav = input("Ingrese el título del proyecto: \n")
        generador_archivos(nombre_archivo_sav, game_name, game_ver, game_dlcs, game_saveFolder_location, game_notes)
    else:
        print ("Saliendo sin guardar. \n")

def lectura_documento():
    archiveName = input("Ingrese el nombre del documento para ver:\n")
    if not archiveName.endswith(".txt"):
            archiveName += ".txt"

    try:
        with open (archiveName, "r", encoding="utf-8") as archivo:
            contenidoLeido = archivo.read()
            return contenidoLeido
    except FileNotFoundError:
        return "Error: documento no encontrado..."
            

#######Comienzo del programa#######
if __name__ == "__main__":

    while create_read_delete != "salir":
        create_read_delete = input("Desea crear / leer / borrar documento? (o salir:)\n").lower()
        if create_read_delete == "crear":
            #crear documento#
            game_name, game_ver, game_dlcs, game_saveFolder_location = solicitud_datos()
            limpiar_pantalla()
            game_notes = nota_final()
            confirmar_generar_documento()

        elif create_read_delete == "leer":
            limpiar_pantalla()
            #Ver documento#
            contenidoMostrar = lectura_documento()
            print(contenidoMostrar)
            input("\nPresiona Enter para volver al menú...")
            
        
    

                                                                                                