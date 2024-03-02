import os
from tabulate import tabulate
def lista(equipos:dict):
    info = []
    for key,value in equipos.items():
        info.append(value)
    print(tabulate(info,headers="keys",tablefmt='grid'))