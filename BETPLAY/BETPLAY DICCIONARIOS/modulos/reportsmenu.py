#### MENU REPORTES ###
import os
def menureportes():
    optionsresults=['A','B','C','D','E','F']
    optionlistresults=['A. EQUIPO GOLEADOR', 'B. EQUIPO CON MAS PUNTOS', 'C. EQUIPO CON MAS PARTIDOS GANADOS', 'D. TOTAL GOLES EN EL TORNEO', 'E. PROMEDIO DE GOLES EN EL TORNEO','F. REGRESAR AL MENU PRINCIPAL']
    titulo2= """
    ++++++++++++++++++++++++++++++++++++++++++++++++
    +++++++++     LIGA BET PLAY REPORTES    ++++++++
    ++++++++++++++++++++++++++++++++++++++++++++++++
    """
    os.system('cls')
    print(titulo2)

    for item2 in optionlistresults:
        print (item2)

    try:
        opr=input('-> ').upper()
        if (opr not in optionsresults):
            menureportes()
    except ValueError:
        print ('ERROR')
        os.system('pause')
        menureportes()
    else:
        return opr

 
