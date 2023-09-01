def mensaje_bienvenido():
    print("Bienvenido al sistema de consulta de propiedades edáficas.")

def pantalla_pedir_datos():
    departamento = input("Ingrese el departamento: ")
    departamento = departamento.upper()
    municipio = input("Ingrese el municipio: ")
    municipio = municipio.upper()
    cultivo = input("Ingrese el tipo de cultivo: ")
    cultivo = cultivo.capitalize()
    limit = int(input("Ingrese el número de registros a consultar: "))
    return departamento, municipio, cultivo, limit

def mostrar_resultados(datos_recuperados, medianas_calculadas):
    print("Resultados:")
    print(datos_recuperados[['departamento', 'municipio', 'cultivo', 'topografia']].to_string(index=False))
    print("Medianas de las variables edáficas:")
    for nombre_variable, valor_mediana in medianas_calculadas.items():
        print(f"{nombre_variable}: {valor_mediana}")