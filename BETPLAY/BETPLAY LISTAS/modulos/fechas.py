import os
fecha = []
def AddGame(lstEquipos:list,lstFechas:list,counter=1):
    msg=''
    os. system('cls')
    titulo ="""
REGISTRO DE FECHA LIGA BETPLAY
    """
    print(titulo)
    for idx, item in enumerate(lstEquipos):  
        print(f'{idx+1}. {str(item[0]).upper()}')
    if(counter == 1):
        msg = 'Seleccione el Equipo Local'
        estado = 'L'
    else:
        msg = 'Seleccione el Equipo Visitante'
        estado = 'V'
    opcion = int(input(f'{msg} :)')) #arreglar para que no se puedan poner cosas que no estan
    goles = int(input(f'Ingrese los goles marcados por {lstEquipos[opcion-1][0]} :')) # arreglar para que no se pongan letras
    fecha. append([lstEquipos[opcion-1][0],goles,estado,(opcion-1)])
    os.system('pause')
    counter += 1
    if (counter<=2):
        AddGame(lstEquipos,lstFechas,counter)
    else:
        if fecha [0][1]>fecha[1][1]:
            lstEquipos[fecha [0][3]][5]+=fecha[0][1] ## goles a favor local
            lstEquipos[fecha [0][3]][6]+=fecha[1][1] ## goles en contra local
            lstEquipos[fecha [1][3]][5]+=fecha[1][1] ## goles a favor visitante
            lstEquipos[fecha [1][3]][6]+=fecha[0][1] ## goles en contra visitante
            lstEquipos[fecha [0][3]][1]+= 1 ## partidos jugados local
            lstEquipos[fecha [1][3]][1]+= 1 ## partidos jugados visitante
            lstEquipos[fecha [0][3]][2]+= 1 ## partidos ganados local
            lstEquipos[fecha [1][3]][3]+= 1 ## partidos perdidos visitante
            lstEquipos[fecha [0][3]][7]+= 1 # puntos local
        
        elif fecha [0][1]<fecha[1][1]:
            lstEquipos[fecha [0][3]][5]+=fecha[0][1] ## goles a favor local
            lstEquipos[fecha [0][3]][6]+=fecha[1][1] ## goles en contra local
            lstEquipos[fecha [1][3]][5]+=fecha[1][1] ## goles a favor visitante
            lstEquipos[fecha [1][3]][6]+=fecha[0][1] ## goles en contra visitante
            lstEquipos[fecha [0][3]][1]+= 1 ## partidos jugados local
            lstEquipos[fecha [1][3]][1]+= 1 ## partidos jugados visitante
            lstEquipos[fecha [0][3]][3]+= 1 ## partidos perdidos local
            lstEquipos[fecha [1][3]][2]+= 1 ## partidos ganados visitante
            lstEquipos[fecha [1][3]][7]+= 3 # puntos local
        else:
            # lstEquipos[fecha [0][3]][5]+=fecha[0][1] ## goles a favor local
            # lstEquipos[fecha [0][3]][6]+=fecha[1][1] ## goles en contra local
            # lstEquipos[fecha [1][3]][5]+=fecha[1][1] ## goles a favor visitante
            # lstEquipos[fecha [1][3]][6]+=fecha[0][1] ## goles en contra visitante
            # lstEquipos[fecha [0][3]][1]+= 1 ## partidos jugados local
            # lstEquipos[fecha [1][3]][1]+= 1 ## partidos jugados visitante
            f1(lstEquipos,fecha)
            lstEquipos[fecha [0][3]][4]+= 1 ## partidos empatados local
            lstEquipos[fecha [1][3]][4]+= 1 ## partidos empatados visitante
            lstEquipos[fecha [0][3]][7]+= 1 # puntos local
            lstEquipos[fecha [0][3]][7]+= 1 # puntos visitante

        nroFecha = int(input('Ingrese el numero de fecha :'))
        lstFechas[nroFecha-1].append (fecha)
        
def f1 (l: list, f: list):
    l[fecha [0][3]][5]+=f[0][1] ## goles a favor local
    l[f [0][3]][6]+=f[1][1] ## goles en contra local
    l[f [1][3]][5]+=f[1][1] ## goles a favor visitante
    l[f [1][3]][6]+=f[0][1] ## goles en contra visitante
    l[f [0][3]][1]+= 1 ## partidos jugados local
    l[f [1][3]][1]+= 1 ## partidos jugados visitante
