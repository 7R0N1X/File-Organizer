import os
import shutil


def banner():
    mensaje = """
                    ::::::::::: :::::::::   :::::::  ::::    :::   :::   :::    ::: 
                    :+:     :+: :+:    :+: :+:   :+: :+:+:   :+: :+:+:   :+:    :+: 
                           +:+  +:+    +:+ +:+  :+:+ :+:+:+  +:+   +:+    +:+  +:+  
                          +#+   +#++:++#:  +#+ + +:+ +#+ +:+ +#+   +#+     +#++:+   
                         +#+    +#+    +#+ +#+#  +#+ +#+  +#+#+#   +#+    +#+  +#+  
                        #+#     #+#    #+# #+#   #+# #+#   #+#+#   #+#   #+#    #+# 
                        ###     ###    ###  #######  ###    #### ####### ###    ### 
                                                                                          
    Este script organizará tus archivos en carpetas según su tipo.
    Puedes encontrar el código en nuestro repositorio de GitHub: https://github.com/7R0N1X/File-Organizer
    """
    print(mensaje)


def organizar_archivos(ruta):
    # Definir tipos de archivos y sus extensiones correspondientes
    tipos_archivos = {
        'Documentos': ['.doc', '.docx', '.xlsx', '.pptx', '.txt', '.pdf'],
        'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.cab', '.tar.gz'],
        'Imágenes': ['.jpg', '.jpeg', '.png', '.gif'],
        'Audios': ['.mp3', '.wav', '.aac', '.flac', '.wma', '.ogg', '.aiff', '.m4a', '.ape'],
        'Videos': ['.mp4', '.avi', '.mkv', '.wmv', '.mov', '.flv', '.3gp', '.webm', '.mpg', '.rmvb'],
        'ISO': ['.iso'],
        'Programas': ['.exe', '.deb', '.rpm', '.msi', '.apk', '.jar']
    }

    # Obtener la lista de archivos en la carpeta principal excluyendo 'FileOrganizer.exe'
    archivos_principales = [archivo for archivo in os.listdir(ruta) if archivo != 'FileOrganizer.exe']

    # Verificar si la carpeta principal está vacía (sin contar 'FileOrganizer.exe')
    if not archivos_principales:
        print("No hay archivos para mover.")
        return

    # Iterar a través de cada tipo de archivo y sus extensiones
    for tipo, extensiones in tipos_archivos.items():
        # Crear la ruta completa a la carpeta para el tipo de archivo
        carpeta_tipo = os.path.join(ruta, tipo)

        # Iterar a través de los archivos en la carpeta principal
        for archivo in archivos_principales:

            # Verificar si el archivo tiene una de las extensiones permitidas
            if archivo.endswith(tuple(extensiones)):
                # Crear la ruta completa al archivo
                ruta_archivo = os.path.join(ruta, archivo)

                # Verificar si ya existe una carpeta para el tipo de archivo
                if not os.path.exists(carpeta_tipo):
                    os.makedirs(carpeta_tipo)

                print(f"Moviendo '{archivo}' a la carpeta '{tipo}'...")
                shutil.move(ruta_archivo, os.path.join(carpeta_tipo, archivo))

    print("Archivos organizados correctamente.")


try:
    ruta_actual = os.getcwd()
    banner()
    input("Presiona Enter para continuar...")
    organizar_archivos(ruta_actual)
except Exception as e:
    print("Ocurrió un error:", str(e))
input("Presiona Enter para salir...")
