import os

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

def generador_archivos(nombre_docuSave, base_data_games):
    try:
        #añade el .txt al final#
        if not nombre_docuSave.endswith(".txt"):
            nombre_docuSave += ".txt"
           
        with open(nombre_docuSave, "w", encoding="utf-8") as f:
            f.write (f"Título: {base_data_games["nombre"]}\n")
            f.write (f"Versión: {base_data_games["version"]}\n")
            f.write (f"DLC(s): {", ".join(base_data_games["dlcs"])}\n")
            f.write (f"Ruta de partidas guardadas: {base_data_games["ruta_saves"]}\n")
            f.write (f"Notas del usuario: {base_data_games["notas"]}\n")
            f.write (f"-" *30 + "\n")
            print(f"Archivo creado en: {os.getcwd()}\\{nombre_docuSave}\n")
    except PermissionError:
        print("error inesperado")
        return base_data_games

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

        #REFACTORIZADO (DICCIONARIO)#
        base_data_games = {
        "nombre": game_name,
        "version": game_ver,
        "dlcs": [d.strip() for d in game_dlcs],
        "ruta_saves": game_saveFolder_location,
        "notas": "Sin notas",
        }

        #pregunta de control#
        confirm_info = input("\nSon estos datos correctos? (s/n)").upper()
        if confirm_info == "S":
            break
        
    return base_data_games

def nota_final():
    yesNote = input("\n¿Desea agregar notas adicionales? (ej: errores de mods, requisitos de hardware, etc.) --S/N--").upper()
    if yesNote == "S":
        game_notes = input("Notas: ")
        return game_notes

def confirmar_generar_documento(base_data_games):
    confirm_save = input("Desea generar un archivo .txt con la información?:...(S - generar archivo/N - salir sin guardar) \n").upper()
    if confirm_save == "S":
        nombre_archivo_sav = input("Ingrese el título del proyecto: \n")
        generador_archivos(nombre_archivo_sav, base_data_games)
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

def añadir_info_documento():
    pass                                #CONTINUAR#

def listar_archivos():
    archivos = [files for files in os.listdir() if files.endswith(".txt")]
    if archivos:
        print("\nDocumentos de juegos encontrados:")
        for archivo in archivos:
            print(f"- {archivo}")
    else:
        print("No se encontraron registros.")

def borrado_documento(nombre_archivo):
    nombre_archivo = input("Ingrese el nombre del documento:\n")
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"
    
    if os.path.exists(nombre_archivo):
        eliminar = input(f"¿Desea borrar el documento {nombre_archivo}? (S/N):\n").upper()
        if eliminar == "S":
            os.remove(nombre_archivo)
            print("Documento removido...")
        else:
            print("Borrado CANCELADO")
    else:
        print("Documento inexistente...")
            

#######Comienzo del programa#######
if __name__ == "__main__":

    while create_read_delete != "salir":
        create_read_delete = input("Desea 'listar' / 'crear' / 'leer' / 'añadir' / 'borrar' documento? (o salir:)\n").lower()
        if create_read_delete == "crear":
            #crear documento#
            base_data_games = solicitud_datos()
            limpiar_pantalla()
            base_data_games["notas"] = nota_final()
            confirmar_generar_documento(base_data_games)

        elif create_read_delete == "leer":
            limpiar_pantalla()
            #Ver documento#
            contenidoMostrar = lectura_documento()
            print(contenidoMostrar)
            input("\nPresiona Enter para volver al menú...")

        elif create_read_delete == "añadir":
            añadir_info_documento()

        elif create_read_delete == "borrar":
            borrado_documento(nombre_archivo_sav)

        elif create_read_delete == "listar":
            listar_archivos()
            
        
    

                                                                                                