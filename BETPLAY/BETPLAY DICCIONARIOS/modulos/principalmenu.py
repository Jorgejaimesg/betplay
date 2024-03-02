#### MENU PRINCIPAL ###
import os

def menu1():
    options=[1,2,3,4,5]
    optionlist=['1. REGISTRAR EQUIPO', '2. LISTA', '3. REGISTRAR FECHA DE JUEGO', '4. REPORTE', '5. SALIR']
    titulo= """
    ++++++++++++++++++++++++++++++++++++++++++++++++
    +++++++++ LIGA BET PLAY MENU PRINCIPAL +++++++++
    ++++++++++++++++++++++++++++++++++++++++++++++++
    """
    os.system('cls')
    print(titulo)

    for item in optionlist:
        print (item)
    try:
        op =int(input('-> '))
        if (op not in options):
            menu1()
    except ValueError:
        print ('ERROR')
        os.system('pause')
        menu1()
    else:
    
        return op