import os
from tabulate import tabulate
def AddTeam(lstEquipos : list):
    nombre = input('Ingrese el nombre del Equipo :')
    lstEquipos.append([nombre,0,0,0,0,0,0,0])
    
def DelTeam(lstEquipos : list):
    palabra = input('Ingrese nombre del equipo a borrar')
    for idx,item in enumerate(lstEquipos):
        if (palabra in item):
            lstEquipos.pop(idx)
            break
def viewTeams(lstEquipos:list):
    lstEquipos.sort(key=lambda item: item[7])
    os.system('clear')
    titulo="""
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    + lista de equipos ++++++++++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    print(tabulate(lstEquipos,headers=['equipo','PJ','PG','PP','PE','GF','GC','TP'],tablefmt='grid'))
    os.system('pause')

