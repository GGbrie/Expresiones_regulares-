import re

buscar = re.findall
concordancia = re.match

# Ejercicio A) Ingresado un texto, extraer/mostrar los correos electrónicos incluidos en él.
def correos(texto):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    correos = buscar(pattern, texto)
    return correos

# Ejercicio B) Extraer/mostrar los comentarios de un código fuente.
def extraer(codigo):
    pattern = r'#.*'
    comentarios = buscar(pattern, codigo, re.MULTILINE)
    return comentarios

# Ejercicio C) Validar fechas válidas, formato mm/dd/yyyy
def validar_fecha(fecha):
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/(\d{4})$'
    si_es_fecha_valida = concordancia(pattern, fecha)
    return si_es_fecha_valida is not None

# Menú de opciones
def menu():
    print("-------------------------------")
    print("Seleccione una opción del menú:")
    print("1. Extraer correos electrónicos de un texto")
    print("2. Extraer comentarios de código fuente")
    print("3. Validar una fecha en formato mm/dd/yyyy")
    print("4. Salir")
    print("-------------------------------")

    opcion = input("Ingrese el número de la opción que desea realizar: ")
    return opcion

def main():
    while True:
        opcion = menu()

        if opcion == '1':
            texto = input("Ingrese un texto que contenga correos electrónicos: ")
            correos_encontrados = correos(texto)
            print("Los Correos encontrados fueron:", correos_encontrados)
        elif opcion == '2':
            codigo = input("Ingrese el código fuente usando #: ")
            comentarios_encontrados = extraer(codigo)
            print("Los Comentarios encontrados fuerron:", comentarios_encontrados)
        elif opcion == '3':
            fecha = input("Ingrese una fecha en formato mm/dd/yyyy: ")
            if validar_fecha(fecha):
                print(f"La fecha: {fecha} si es una fecha válida en el formato permitido")
            else:
                print(f"ERROR: {fecha} no es una fecha válida. Vuelve a intentarlo.")
        elif opcion == '4':
            print("Saliendo del programa...     ------------------- Gracias -------------------")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
if __name__ == "__main__":
    main()