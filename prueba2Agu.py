precio = 0
kilos_totales = 0
camiones = 0
datos_personales = {}
#definir obtener nombre
def obtener_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre) > 3:
            datos_personales["Nombre"] = nombre
            return nombre
        else:
            print("Ingrese un nombre válido (más de 3 caracteres).")
#definir obtener telefono
def obtener_telefono():
    while True:
        telefono = input("Ingrese su teléfono: ")
        if telefono.isdigit() and 8 <= len(telefono) <= 9:
            datos_personales["Teléfono"] = telefono
            return telefono
        else:
            print("El teléfono debe tener entre 8 y 9 dígitos numéricos, intente otra vez.")
#definir camion estandar
def camion_estandar():
    global precio, kilos_totales, camiones
    print("El camión estándar tiene un valor de $765.000 y contiene:")
    print("- 12 cilindros de 5 kilos")
    print("- 20 cilindros de 15 kilos")
    print("- 2 cilindros de 45 kilos")
    while True:
        try:
            cantidad_camiones = int(input("Seleccione la cantidad de camiones que desea: "))
            if cantidad_camiones > 0:
                print(f"Has agregado {cantidad_camiones} camiones")
                precio = 765000 * cantidad_camiones
                kilos_totales = 450 * cantidad_camiones
                camiones = cantidad_camiones
                return cantidad_camiones
            else:
                print("Debe seleccionar al menos 1 camión.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero, intente otra vez.")
#definir compra carga especifica
def compra_carga_especifica():
    global kilos_totales, precio, camiones
    print("Ingrese la cantidad de cilindros que requiere:")
    cinco_kilos = int(input("Cilindros de 5 kilos: "))
    quince_kilos = int(input("Cilindros de 15 kilos: "))
    cuarentaycinco_kilos = int(input("Cilindros de 45 kilos: "))
    kilos_totales = cinco_kilos + quince_kilos * 3 + cuarentaycinco_kilos * 9

    if kilos_totales <= 450:
        precio = 765000
        camiones = 1
    else:
        camiones = (kilos_totales // 450) + 1
        precio = camiones * 765000

    return cinco_kilos, quince_kilos, cuarentaycinco_kilos

def imprimir_boleta():
    global precio
    if precio == 0:
        print("Aún no has agregado ningún camión.")
    else:
        print("-" * 30)
        print("              DETALLE BOLETA")
        print("-" * 30)
        for clave, valor in datos_personales.items():
            print(f"{clave}: {valor}")
        print(f"Kilos totales: {kilos_totales}")
        print(f"Camiones: {camiones}")
        print(f"Valor total: ${precio}")

def menu():
    while True:
        print("Seleccione la opción:")
        print("1.- Compra entrega camión estándar")
        print("2.- Compra entrega carga específica")
        print("3.- Imprimir boleta y cerrar pedido")
        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                camion_estandar()
            elif opcion == 2:
                compra_carga_especifica()
            elif opcion == 3:
                imprimir_boleta()
                return False
            else:
                print("Selección incorrecta. Por favor, seleccione una opción entre 1 y 3.")
        except ValueError:
            print("Entrada inválida. Por favor, seleccione una opción entre 1 y 3.")

        otra_accion = input("¿Desea realizar otra acción? (si/no): ").strip().lower()
        if otra_accion != 'si':
            imprimir_boleta()
            print("Hasta pronto")
            return False
#definir menu principal
def menu_principal():
    obtener_nombre()
    obtener_telefono()
    while True:
        if not menu():
            break
        otro_pedido = input("¿Desea realizar otro pedido? (si/no): ").strip().lower()
        if otro_pedido != 'si':
            print("Hasta pronto")
            break
#llamada al menu principal
menu_principal()
