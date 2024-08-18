import subprocess
import os
import dropbox # type: ignore


# Obtener los valores del DNI y la dificultad de las variables de entorno.
dni = os.environ.get('DNI')
seleccion = os.environ.get('SELECCION')


# Verificamos que la dificultad del escenario y el DNI están bien definidos.
if dni is None:
    raise ValueError("La variable de entorno 'DNI' no está definida")
if seleccion is None:
    raise ValueError("La variable de entorno 'SELECCION' no está definida")


# Definir la variable de dificultad basada en el valor de 'SELECCION'.
if seleccion == '1':
    dificultad = 'difFacil'
elif seleccion == '2':
    dificultad = 'difMedia'
elif seleccion == '3':
    dificultad = 'difAvanzada'
else:
    raise ValueError("El valor de 'SELECCION' no es válido")


# Funcion que añade la vagrant box en el repositorio local de vagrant.
def agregar_box_vagrant(ruta_box, nombre):
    try:
        # Ejecutar el comando vagrant box add con la ruta de la box como argumento
        resultado = subprocess.run(['vagrant', 'box', 'add', nombre, ruta_box], capture_output=True, text=True)
        
        # Comprobar si la ejecución del comando fue exitosa
        if resultado.returncode == 0:
            print("La box se agregó correctamente a Vagrant.")
        else:
            print("Ocurrió un error al agregar la box a Vagrant:")
            print(resultado.stderr)
    except Exception as e:
        print("Ocurrió un error al ejecutar el comando de Vagrant:")
        print(str(e))


# Instalación de la librería de python para Dropbox.
print("\n")
print("INSTALANDO LIBRERIA DROPBOX API PARA PYTHON")
subprocess.run(["pip", "install", "dropbox"])
print("\n")


# token de acceso personal de Dropbox
with open("TOKEN.txt", "r") as f:
    token = f.read()


# Carpeta en Dropbox donde se guardarán los archivos
DROPBOX_FOLDER = "/Boxes"


# Ruta local donde se guardarán los archivos descargados
LOCAL_FOLDER = "Boxes"


# Conexión con la API de Dropbox
dbx = dropbox.Dropbox(token)


# Iterar sobre los valores de i de 1 a 10
for i in range(1, 11):
    # Construir el nombre del archivo esperado para este valor de i
    filename = f"vm{i}_{dni}_difAvanzada.box"

    # Verificar si el archivo está en la lista de archivos en la carpeta de Dropbox
    files_list = dbx.files_list_folder(DROPBOX_FOLDER)
    for entry in files_list.entries:
        if entry.name == filename:
            # Construir la ruta remota del archivo en Dropbox
            remote_path = f"{DROPBOX_FOLDER}/{entry.name}"

            # Construir la ruta local donde se guardará el archivo
            local_path = os.path.join(LOCAL_FOLDER, entry.name)

            # Descargar el archivo desde Dropbox
            dbx.files_download_to_file(local_path, remote_path)

            print(f"Archivo '{entry.name}' descargado correctamente.")

            agregar_box_vagrant(local_path, f"vm{i}_{dni}_difAvanzada")

print("Descarga de archivos completada.")


# Desplegamos las 5 máquinas virtuales, sin aprovisionamiento y sin iniciar sesión en ellas => (no destroy on error)
subprocess.run(["vagrant", "up", f"vm1_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm2_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm3_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm4_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm5_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm6_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm7_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm8_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm9_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")
subprocess.run(["vagrant", "up", f"vm10_{dni}_{dificultad}", "--no-destroy-on-error", "--no-provision"], stderr=subprocess.DEVNULL)
print("\n")