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
        'PDF': ['.pdf'],
        'Documentos': ['.doc', '.docx', '.txt'],
        'Hojas de cálculos': ['.xlsx'],
        'Presentaciones': ['.pptx'],
        'Imagenes': ['.jpg', '.jpeg', '.png', '.gif'],
        'MP3': ['.mp3'],
        'MP4': ['.mp4'],
        'ISO': ['.iso'],
        'Programas': ['.exe']
    }

    # Iterar a través de cada tipo de archivo y sus extensiones
    for tipo, extensiones in tipos_archivos.items():
        # Crear la ruta completa a la carpeta para el tipo de archivo
        carpeta_tipo = os.path.join(ruta, tipo)

        # Iterar a través de los archivos en la carpeta principal
        for archivo in os.listdir(ruta):
            # Verificar si el archivo tiene una de las extensiones permitidas
            if archivo != 'FileOrganizer.exe' and archivo.endswith(tuple(extensiones)):
                # Crear la ruta completa al archivo
                ruta_archivo = os.path.join(ruta, archivo)

                # Verificar si ya existe una carpeta para el tipo de archivo
                if not os.path.exists(carpeta_tipo):
                    os.makedirs(carpeta_tipo)

                print(f"Moviendo '{archivo}' a la carpeta '{tipo}'...")
                shutil.move(ruta_archivo, os.path.join(carpeta_tipo, archivo))


try:
    ruta_actual = os.getcwd()
    banner()
    input("Presiona Enter para continuar...")
    organizar_archivos(ruta_actual)
    print("Archivos organizados correctamente.")
except Exception as e:
    print("Ocurrió un error:", str(e))
input("Presiona Enter para salir...")
