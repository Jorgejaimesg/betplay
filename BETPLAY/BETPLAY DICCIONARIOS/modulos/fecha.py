import os


def fechas(equipos:list):
    for key,value in equipos.items():
        print(f'{key}. {(value["nombre"])}')
        options=list(range(1, len(equipos) + 1))
        
######## PIDO LOS DATOS #############################################################################################################
    isTheSame=True
    while isTheSame==True:
        el=int(input('seleccione el equipo local: '))
        eV=int(input('seleccione el equipo Visitante: '))
        if (el == eV)or(el not in options)or(eV not in options):
            print('datos invalidos')
            os.system('pause')
        else:
             isTheSame=False

    golL=solicitar_goll(equipos,el)
    golV=solicitar_goll(equipos,eV)

########## EVALUO LOS PARTIDOS ###################################################################################################

    if golL>golV:
        actualizartablas(equipos[el],golV,golL,'G')
        actualizartablas(equipos[eV],golL,golV,'P')
    elif golL<golV:
        
        actualizartablas(equipos[el],golV,golL,'P')
        actualizartablas(equipos[eV],golL,golV,'G')
    else:
        
        actualizartablas(equipos[el],golV,golL,'E')
        actualizartablas(equipos[eV],golL,golV,'E')

####### ACTTUALIZO LA TABLA DEPENDIENDO DEL PARTIDO, CADA EQUIPO SE ACTUALIZA INDIVIDUALMENTE  ######################################

def actualizartablas(equipo,golesContra,golesaFavor,resultado):
    equipo['PJ']+=1
    equipo['GC']+=golesContra
    equipo['GF']+=golesaFavor

    if resultado == 'G':
        equipo['PG']+=1
        equipo['TP']+=3
    elif resultado =='P':
        equipo['PP']+=1       
    else:
        equipo['PE']+=1
        equipo['TP']+=1

def solicitar_goll(equipos,name):
            while True:
                    try:
                        opcion = int(input(f"cuantos goles metio el equipo {equipos[name]['nombre']}: "))
                        return opcion
                    except ValueError:
                        print('datos invalidos')
                        os.system('cls')