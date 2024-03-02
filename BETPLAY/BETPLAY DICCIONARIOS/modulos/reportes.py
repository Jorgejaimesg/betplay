import os
def reportes(equipos,x,msg):
   maxd=equipos[max(equipos, key=lambda llave: equipos[llave][x])]['nombre']
   print (f'{msg} {maxd}')

def total(equipos,x):
   resultado=sum(equipo[x] for equipo in equipos.values())
   return resultado