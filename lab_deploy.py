import re
import os
import hashlib


print("--------------------------------------------------------------------------------------")
os.system("chmod 777 Animations/1.sh")
os.system("Animations/1.sh")
print("--------------------------------------------------------------------------------------")


# Función para validar el formato del DNI.
def validar_dni(dni):
    # Patrón de expresión regular para un DNI válido.
    patron_dni = r'^\d{8}[a-zA-Z]$'
    return re.match(patron_dni, dni) is not None


# Solicitar el DNI como input repetidamente hasta que sea válido.
dni_valido = False
while not dni_valido:
    dni = input("Por favor, introduce tu DNI: .......... ")
    if validar_dni(dni):
        dni_valido = True
    else:
        print("- !FORMATO DE DNI NO VALIDO! Debe tener 9 caracteres, 8 numeros seguidos de una letra.")
print("- ¡DNI introducido correctamente! -> {}".format(dni))
print("--------------------------------------------------------------------------------------")


# Imprimir el menú de selección de dificultad.
print("\n")
print("Selecciona la dificultad:")
print("(1) DIFICULTAD FACIL")
print("|     -> 1 maquina atacante")
print("|     -> 4 maquinas que hackear")
print("|     -> 4 banderas")
print("|     -> X pistas")
print("(2) DIFICULTAD MEDIA")
print("|     -> 1 maquina atacante")
print("|     -> 8 maquinas que hackear")
print("|     -> 8 banderas")
print("|     -> X pistas")
print("(3) DIFICULTAD AVANZADA")
print("|     -> 1 maquina atacante")
print("|     -> 9 maquinas que hackear")
print("|     -> 9 banderas")
print("|     -> X pistas")


# Selección de dificultad.
seleccion = None
while True:
    seleccion = input("Ingresa el numero correspondiente a la dificultad que deseas: .......... ")

    if seleccion in ["1", "2", "3"]:
        break
    else:
        print("- !SELECCION NO VALIDA!")


# Mensaje correspondiente a la selección
mensaje_seleccionado = ""
if seleccion == "1":
    mensaje_seleccionado = "DIFICULTAD FACIL"
elif seleccion == "2":
    mensaje_seleccionado = "DIFICULTAD MEDIA"
elif seleccion == "3":
    mensaje_seleccionado = "DIFICULTAD AVANZADA"


# Imprimir el mensaje con la dificultad seleccionada
print("- ¡Dificultad seleccionada correctamente! -> ({}) {}".format(seleccion, mensaje_seleccionado))
print("--------------------------------------------------------------------------------------")
print("\n")


# Función para generar las IPs del escenario.
def generate_ip_addresses(dni, seleccion):
    # Calcula el hash basado en el DNI y la dificultad.
    hash_value = hashlib.md5(f"{dni}{seleccion}".encode()).hexdigest()

    # Extraer el primer carácter del hash y convertirlo a un entero.
    num = int(hash_value[0], 16)

    # Asegurar que el número esté dentro del rango 0-4.
    num %= 5

    # Definir la base de la dirección IP.
    base_ip_RED_PRUEBAS = "192.168.56.5"
    base_ip_RED_PRE_PRODUCCION = "192.168.56."
    base_ip_RED_PRODUCCION = "192.168.56.20"

    # Generar las direcciones IP para las máquinas vm1, vm2, vm3, vm4 y vm5.
    ip_vm1 = f"{base_ip_RED_PRUEBAS}{num}"
    ip_vm2 = f"{base_ip_RED_PRUEBAS}{(num + 1) % 5}"  # Asegura que sea diferente de vm1.
    ip_vm3 = f"{base_ip_RED_PRUEBAS}{(num + 2) % 5}"  # Asegura que sea diferente de vm1 y vm2.
    ip_vm4 = f"{base_ip_RED_PRUEBAS}{(num + 3) % 5}"  # Asegura que sea diferente de vm1, vm2 y vm3.
    ip_vm5_1 = f"{base_ip_RED_PRUEBAS}{(num + 4) % 5}"  # Asegura que sea diferente de vm1, vm2, vm3 y vm4.

    # Generar las direcciones IP para las máquinas vm5, vm6, vm7, vm8 y vm9.
    ip_vm5_2 = f"{base_ip_RED_PRE_PRODUCCION}{97 + num}"
    ip_vm6 = f"{base_ip_RED_PRE_PRODUCCION}{98 + (num + 1) % 5}"  # Asegura que sea diferente de vm5.
    ip_vm7 = f"{base_ip_RED_PRE_PRODUCCION}{99 + (num + 2) % 5}"  # Asegura que sea diferente de vm5 y vm6.
    ip_vm8 = f"{base_ip_RED_PRE_PRODUCCION}{100 + (num + 3) % 5}"  # Asegura que sea diferente de vm5, vm6 y vm7.
    ip_vm9_1 = f"{base_ip_RED_PRE_PRODUCCION}{101 + (num + 4) % 5}"  # Asegura que sea diferente de vm5, vm6, vm7 y vm8.

    # Generar las direcciones IP para las máquinas vm9 y vm10.
    ip_vm9_2 = f"{base_ip_RED_PRODUCCION}{1 + num}"
    ip_vm10 = f"{base_ip_RED_PRODUCCION}{2 + (num + 1) % 2}"  # Asegura que sea diferente de vm9.

    # Exportar las IPs como variables de entorno.
    os.environ['IP_VM1'] = ip_vm1
    os.environ['IP_VM2'] = ip_vm2
    os.environ['IP_VM3'] = ip_vm3
    os.environ['IP_VM4'] = ip_vm4
    os.environ['IP_VM5_1'] = ip_vm5_1
    os.environ['IP_VM5_2'] = ip_vm5_2
    os.environ['IP_VM6'] = ip_vm6
    os.environ['IP_VM7'] = ip_vm7
    os.environ['IP_VM8'] = ip_vm8
    os.environ['IP_VM9_1'] = ip_vm9_1
    os.environ['IP_VM9_2'] = ip_vm9_2
    os.environ['IP_VM10'] = ip_vm10

    return {
        'IP_VM1': ip_vm1,
        'IP_VM2': ip_vm2,
        'IP_VM3': ip_vm3,
        'IP_VM4': ip_vm4,
        'IP_VM5_1': ip_vm5_1,
        'IP_VM5_2': ip_vm5_2,
        'IP_VM6': ip_vm6,
        'IP_VM7': ip_vm7,
        'IP_VM8': ip_vm8,
        'IP_VM9_1': ip_vm9_1,
        'IP_VM9_2': ip_vm9_2,
        'IP_VM10': ip_vm10,
    }


def generar_usuario_y_contraseña_vm1(dni, seleccion):
    # Concatenar DNI y SELECCION
    hash_value_vm1 = hashlib.md5(f"{dni}{seleccion}".encode()).hexdigest()
    
    # Extraer los primeros dos caracteres del hash para el nombre de usuario
    user_suffix = hash_value_vm1[:2]
    username = f"Attack{user_suffix}"
    
    # Extraer los últimos 12 caracteres del hash para la contraseña
    password = hash_value_vm1[-12:]
    
    return username, password


# Generamos las IPs del escenario.
ip_addresses = generate_ip_addresses(dni, seleccion)


# Generar nombre de usuario y contraseña
usuario, contraseña = generar_usuario_y_contraseña_vm1(dni, seleccion)


# Establecer el DNI como variable de entorno
os.environ["SELECCION"] = seleccion
os.environ["DNI"] = dni

# Exportar el nombre de usuario y la contraseña como variables de entorno
os.environ['VM1_USERNAME'] = usuario
os.environ['VM1_PASSWORD'] = contraseña


# Solicitar al usuario que elija una opción
print("{}".format(mensaje_seleccionado))
print("-----------------------")
print("Selecciona una opcion:")
print("(1)  -> Apagar Escenario")
print("(2)  -> Detener Escenario")
print("(3)  -> Eliminar Escenario")
print("(4)  -> Iniciar Escenario")
print("(5)  -> Instalar Escenario")
print("(6)  -> Cambiar Dificultad Escenario")
print("(7)  -> Informacion acerca del Escenario")
print("(8)  -> SALIR")


# Verificar si la opción ingresada es válida
opcion = None
while True:
    opcion = input("Ingresa el numero correspondiente a la accion que deseas realizar: .......... ")

    if opcion in ["1", "2", "3", "4", "5","6", "7", "8"]:
        break
    else:
        print("- !SELECCION NO VALIDA!")


continuar = True
while (continuar == True):
    # Dificultad fácil
    if (opcion == "1" and seleccion=="1"):
        print("- (1) -> EJECUTANDO SCRIPT: apagarEscenario.py")
        os.system("python3 DeployScripts/Dificultad1-Facil/apagarEscenario.py")
        print("- (1) -> !ESCENARIO DIFICULTAD FACIL APAGADO!")
    elif (opcion == "2" and seleccion=="1"):
        print("- (2) -> EJECUTANDO SCRIPT: detenerEscenario.py")
        os.system("python3 DeployScripts/Dificultad1-Facil/detenerEscenario.py")
        print("- (2) -> !ESCENARIO DIFICULTAD FACIL DETENIDO!")
    elif (opcion == "3" and seleccion=="1"):
        print("- (3) -> EJECUTANDO SCRIPT: eliminarEscenario.py")
        os.system("python3 DeployScripts/Dificultad1-Facil/eliminarEscenario.py")
        print("- (3) -> !ESCENARIO DIFICULTAD FACIL ELIMINADO!")
    elif (opcion == "4" and seleccion=="1"):
        print("- (4) -> EJECUTANDO SCRIPT: iniciarEscenario.py")
        os.system("python3 DeployScripts/Dificultad1-Facil/iniciarEscenario.py")
        print("- (4) -> !ESCENARIO DIFICULTAD FACIL INICIADO!")
    elif (opcion == "5" and seleccion=="1"):
        print("- (5) -> EJECUTANDO SCRIPT: instalarEscenario.py")
        os.system("python3 DeployScripts/Dificultad1-Facil/instalarEscenario.py")
        print("- (5) -> !ESCENARIO DIFICULTAD FACIL INSTALADO!")
    elif (opcion == "7" and seleccion=="1"):
        print("- (7) -> EJECUTANDO SCRIPT: informacionEscenario.py")
        print("\n")
        print("DOCUMENTACION DIFICULTAD FACIL")
        os.system("python3 DeployScripts/Dificultad1-Facil/informacionEscenario.py")

    # Dificultad media
    if (opcion == "1" and seleccion=="2"):
        print("- (1) -> EJECUTANDO SCRIPT: apagarEscenario.py")
        os.system("python3 DeployScripts/Dificultad2-Media/apagarEscenario.py")
        print("- (1) -> !ESCENARIO DIFICULTAD MEDIA APAGADO!")
    elif (opcion == "2" and seleccion=="2"):
        print("- (2) -> EJECUTANDO SCRIPT: detenerEscenario.py")
        os.system("python3 DeployScripts/Dificultad2-Media/detenerEscenario.py")
        print("- (2) -> !ESCENARIO DIFICULTAD MEDIA DETENIDO!")
    elif (opcion == "3" and seleccion=="2"):
        print("- (3) -> EJECUTANDO SCRIPT: eliminarEscenario.py")
        os.system("python3 DeployScripts/Dificultad2-Media/eliminarEscenario.py")
        print("- (3) -> !ESCENARIO DIFICULTAD MEDIA ELIMINADO!")
    elif (opcion == "4" and seleccion=="2"):
        print("- (4) -> EJECUTANDO SCRIPT: iniciarEscenario.py")
        os.system("python3 DeployScripts/Dificultad2-Media/iniciarEscenario.py")
        print("- (4) -> !ESCENARIO DIFICULTAD MEDIA INICIADO!")
    elif (opcion == "5" and seleccion=="2"):
        print("- (5) -> EJECUTANDO SCRIPT: instalarEscenario.py")
        os.system("python3 DeployScripts/Dificultad2-Media/instalarEscenario.py")
        print("- (5) -> !ESCENARIO DIFICULTAD MEDIA INSTALADO!")
    elif (opcion == "7" and seleccion=="2"):
        print("- (7) -> EJECUTANDO SCRIPT: informacionEscenario.py")
        print("\n")
        print("DOCUMENTACION DIFICULTAD MEDIA")
        os.system("python3 DeployScripts/Dificultad2-Media/informacionEscenario.py")

    # Dificultad avanzada
    if (opcion == "1" and seleccion=="3"):
        print("- (1) -> EJECUTANDO SCRIPT: apagarEscenario.py")
        os.system("python3 DeployScripts/Dificultad3-Avanzada/apagarEscenario.py")
        print("- (1) -> !ESCENARIO DIFICULTAD AVANZADA APAGADO!")
    elif (opcion == "2" and seleccion=="3"):
        print("- (2) -> EJECUTANDO SCRIPT: detenerEscenario.py")
        os.system("python3 DeployScripts/Dificultad3-Avanzada/detenerEscenario.py")
        print("- (2) -> !ESCENARIO DIFICULTAD AVANZADA DETENENIDO!")
    elif (opcion == "3" and seleccion=="3"):
        print("- (3) -> EJECUTANDO SCRIPT: eliminarEscenario.py")
        os.system("python3 DeployScripts/Dificultad3-Avanzada/eliminarEscenario.py")
        print("- (3) -> !ESCENARIO DIFICULTAD AVANZADA ELIMINADO!")
    elif (opcion == "4" and seleccion=="3"):
        print("- (4) -> EJECUTANDO SCRIPT: iniciarEscenario.py")
        os.system("python3 DeployScripts/Dificultad3-Avanzada/iniciarEscenario.py")
        print("- (4) -> !ESCENARIO DIFICULTAD AVANZADA INICIADO!")
    elif (opcion == "5" and seleccion=="3"):
        print("- (5) -> EJECUTANDO SCRIPT: instalarEscenario.py")
        os.system("python3 DeployScripts/Dificultad3-Avanzada/instalarEscenario.py")
        print("- (5) -> !ESCENARIO DIFICULTAD AVANZADA INSTALADO!")
    elif (opcion == "7" and seleccion=="3"):
        print("- (7) -> EJECUTANDO SCRIPT: informacionEscenario.py")
        print("\n")
        print("DOCUMENTACION DIFICULTAD AVANZADA")
        os.system("python3 DeployScripts/Dificultad3-Avanzada/informacionEscenario.py")

    elif (opcion == "6"):
        print("\n")
        print("- (6) -> !SELECCIONE NUEVO NIVEL DE DIFICULTAD!")
        print("(1) DIFICULTAD FACIL")
        print("|     -> 1 maquina atacante")
        print("|     -> 4 maquinas que hackear")
        print("|     -> 4 banderas")
        print("|     -> X pistas")
        print("(2) DIFICULTAD MEDIA")
        print("|     -> 1 maquina atacante")
        print("|     -> 8 maquinas que hackear")
        print("|     -> 8 banderas")
        print("|     -> X pistas")
        print("(3) DIFICULTAD AVANZADA")
        print("|     -> 1 maquina atacante")
        print("|     -> 9 maquinas que hackear")
        print("|     -> 9 banderas")
        print("|     -> X pistas")

        seleccion = None
        while True:
            seleccion = input("Ingresa el numero correspondiente a la dificultad que deseas: .......... ")

            if seleccion in ["1", "2", "3"]:
                os.environ["SELECCION"] = seleccion
                break
            else:
                print("- !SELECCION NO VALIDA!")

        # Generamos las IPs del escenario.
        ip_addresses = generate_ip_addresses(dni, seleccion)

        # Generar nombre de usuario y contraseña
        usuario, contraseña = generar_usuario_y_contraseña_vm1(dni, seleccion)

        # Establecer el DNI como variable de entorno
        os.environ["SELECCION"] = seleccion
        os.environ["DNI"] = dni

        # Exportar el nombre de usuario y la contraseña como variables de entorno
        os.environ['VM1_USERNAME'] = usuario
        os.environ['VM1_PASSWORD'] = contraseña

        # Mensaje correspondiente a la selección
        mensaje_seleccionado = ""
        if seleccion == "1":
            mensaje_seleccionado = "DIFICULTAD FACIL"
        elif seleccion == "2":
            mensaje_seleccionado = "DIFICULTAD MEDIA"
        elif seleccion == "3":
            mensaje_seleccionado = "DIFICULTAD AVANZADA"

        # Imprimir el mensaje con la dificultad seleccionada
        print("- ¡Dificultad cambiada correctamente! -> ({}) {}".format(seleccion, mensaje_seleccionado))


    elif (opcion == "8"):
        continuar = False
        break

    while True:
        print("--------------------------------------------------------------------------------------")
        print("\n")
        print("¿Desea realizar alguna otra accion?")
        print("(1) -> SI")
        print("(2) -> NO")
        continuar2 = input("Ingresa el numero correspondiente: ")

        if continuar2 == "2":
            print("- SE HA SALIDO DEL LABORATORIO EXITOSAMENTE")
            print("--------------------------------------------------------------------------------------")
            continuar == False
            break
        elif (continuar2 != "1" and continuar2 != "2"):
            print("- !SELECCION NO VALIDA!")
        else:
            print("--------------------------------------------------------------------------------------")
            print("\n")
            # Solicitar al usuario que elija una opción
            print("{}".format(mensaje_seleccionado))
            print("-----------------------")
            print("Selecciona una opcion:")
            print("(1)  -> Apagar Escenario")
            print("(2)  -> Detener Escenario")
            print("(3)  -> Eliminar Escenario")
            print("(4)  -> Iniciar Escenario")
            print("(5)  -> Instalar Escenario")
            print("(6)  -> Cambiar Dificultad Escenario")
            print("(7)  -> Informacion acerca del Escenario")
            print("(8)  -> SALIR")
            opcion = input("Ingresa el numero correspondiente a la accion que deseas realizar: .......... ")
            continuar == True
            break
    if continuar2 == "2":
        break

print("SE HA SALIDO CORRECTAMENTE")