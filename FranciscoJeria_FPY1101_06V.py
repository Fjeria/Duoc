import random, os, time

ciudadanos = {}

def validar_nif(nif):
    if len(nif) != 12:
        return False
    
    numero = nif[:8]
    guion = nif[8]
    ciudad = nif[9:].upper()
    
    if not numero.isdigit():
        return False
    if guion != '-':
        return False
    if ciudad not in ['MAD', 'BAR', 'SEV']:
        return False
    
    return True

def grabar():
    os.system("clear")
    nif = input("Ingrese NIF (Formato: 12345678-XXX): ").upper()
    if not validar_nif(nif):
        print("NIF inválido. Debe tener el formato 12345678-XXX y pertenecer a MAD, BAR o SEV.")
        return
    
    nombre = input("Ingrese nombre: ")
    if len(nombre) < 8:
        print("Nombre inválido. Debe tener al menos 8 caracteres.")
        return
    
    nacionalidad = input("Ingrese nacionalidad: ")
    
    try:
        edad = int(input("Ingrese edad: "))
        if edad < 15:
            print("Edad inválida. Debe tener 15 o más años.")
            return
    except ValueError:
        print("Edad inválida. Debe ser un número entero")
        return
    
    ciudadanos[nif] = {
        'nif': nif,
        'nombre': nombre,
        'nacionalidad': nacionalidad,
        'edad': edad
    }
    print("Datos guardados correctamente.")
    time.sleep(1.5)
    os.system("clear")

def buscar():
    os.system("clear")
    nif = input("Ingrese el NIF a buscar: ").upper()
    if nif in ciudadanos:
        print(f"NIF: {nif}")
        print(f"Nombre: {ciudadanos[nif]['nombre']}")
        print(f"Edad: {ciudadanos[nif]['edad']}")
        print(f"Nacionalidad: {ciudadanos[nif]['nacionalidad']}")
    else:
        print("\nNo se encontraron datos para el NIF ingresado.")

def imprimir_certificados():
    os.system("clear")
    nif = input("Ingrese el NIF para imprimir certificados: ").upper()
    if nif in ciudadanos:
        ciudadano = ciudadanos[nif]
        salario_mensual = random.randint(1000,5000)
        certificados = {
            "Certificado de Nacimiento": f"Nombre: {ciudadano['nombre']}, NIF: {nif}, Nacionalidad: {ciudadano['nacionalidad']}, Edad: {ciudadano['edad']}",
            "Certificado de Estado Conyugal": f"Nombre: {ciudadano['nombre']}, NIF: {nif}, Estado Conyugal: Soltero(a)",
            "Certificado de Salario Mensual": f"Nombre: {ciudadano['nombre']}, NIF: {nif}, Salario Mensual: {salario_mensual} Euros"
        }
        
        for titulo, contenido in certificados.items():
            print(f"\n{titulo}")
            print(contenido)
    else:
        print("\nNo se encontraron datos para el NIF ingresado.")

def salir():
    os.system("clear")
    print("Saliendo del programa.")
    time.sleep(1)
    os.system("clear")
    print("Saliendo del programa..")
    time.sleep(1)
    os.system("clear")
    print("Saliendo del programa...")
    time.sleep(1)
    os.system("clear")
    print("Hasta pronto")
    exit()

def mostrar_menu():
    while True:
        print("\nRegistro de ciudadanos de la UE en España")
        print("1. Grabar")
        print("2. Buscar")
        print("3. Imprimir certificados")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            grabar()
        elif opcion == '2':
            buscar()
        elif opcion == '3':
            imprimir_certificados()
        elif opcion == '4':
            salir()
        else:
            print("Opción invalida. Por favor, seleccione una opción del menú.")

mostrar_menu()