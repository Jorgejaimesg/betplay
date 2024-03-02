import os
equipos={
     'nombre':'',
     'PJ':'',
     'PG':'',
     'PE':'',
     'PP':'',
     'GF':'',
     'GC':'',
     'TP':''
 }

def AddTeams(equipos: dict):


    isTheSame=True
    while isTheSame==True:
        nombre=input('Ingrese el nombre del equipo que quiere añadir: ')
        for equipo in equipos.values():
            if equipo['nombre']==nombre:
                print('el equipo ya se encuentra registrado:')
                os.system('pause')
                os.system('cls')
                break
                
        else:
            isTheSame=False
        
    PJ=int(0)
    PG=int(0)
    PE=int(0)
    PP=int(0)
    GF=int(0)
    GC=int(0)
    TP=int(0)

    equipo={
        'nombre':nombre,
    'PJ':PJ,
    'PG':PG,
    'PE':PE,
    'PP':PP,
    'GF':GF,
    'GC':GC,
    'TP':TP
    }

    equipos.update({(len(equipos)+1):equipo})
