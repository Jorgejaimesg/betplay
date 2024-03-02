import os

def CrearMenu():
    lstOpciones = [1,2,3,4,5]
    titulo = """
        ++++++++++++++++++++++++++++
        +   LIGA BETPLAY MENU      +
        ++++++++++++++++++++++++++++
    """
    os.system('cls')
    print(titulo)
    try:
        opciones = "1. Agregar equipo\n2. tablas\n3. Registrar Fecha\n4. Reportes\n5. salir"
        print(opciones)
        op =int(input(':) '))
        if (op not in lstOpciones):
            CrearMenu()
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        CrearMenu()
    else:
        return op


    