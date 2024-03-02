
import modulos.principalmenu as menuP
import modulos.reportsmenu as menuR
import modulos.agregarEquipo as e
import modulos.verLista as l
import modulos.fecha as f
import modulos.reportes as r

if __name__ =='__main__':

    equipos={}
    isApprunning=True
    while isApprunning:
        op=menuP.menu1()

#######################################################################################################################################
        
        if (op==1):
            isAddTeam=True
            while isAddTeam:
                f.os.system('cls')
                e.AddTeams(equipos)
                e.os.system('cls')
                isAddTeam=bool(input('Quieres agregar otro equipo S[si] o Enter[no]'))
                e.os.system('cls')

#########################################################################################################################################
        if (op==2):
            l.os.system('cls')
            l.lista(equipos)
            l.os.system('pause')

###########################################################################################################################################

        if (op==3):
            f.os.system('cls')
            f.fechas(equipos)    

###########################################################################################################################################

        if (op==4):
            isReporting=True
            while isReporting:
                opr=menuR.menureportes()
                if (opr=='A'): ## EQUIPO GOLEADOR
                    f.os.system('cls')
                    r.reportes(equipos,'GF','EL EQUIPO CON MAS GOLES ANOTADOS ES: ')
                    l.os.system('pause')

                if (opr=='B'): ## EQUIPO CON MAS PUNTOS
                    f.os.system('cls')
                    r.reportes(equipos,'TP','EL EQUIPO CON MAS PUNTOS ES: ')
                    l.os.system('pause')
                    
                if (opr=='C'):
                    f.os.system('cls') ## EQUIPO CON MAS PARTIDOS GANADOS
                    r.reportes(equipos,'PG','EL EQUIPO CON MAS PARTIDOS GANADOS ES: ')
                    l.os.system('pause')

                if (opr=='D'):
                    f.os.system('cls')
                    tg=r.total(equipos,'GF') ## SUMA DE GOLES TORNEO
                    print(f'EL TOTAL DE GOLES ANOTADOS EN EL TORNEO FUE: {tg}')
                    l.os.system('pause')
                    
                    pass
                if (opr=='E'):
                    f.os.system('cls') ## PROMEDIO DE GOLES TORNEO
                    tg=r.total(equipos,'GF')
                    tp=r.total(equipos,'PJ')/2
                    promedio=tg/tp
                    print(f'EL PROMEDIO DE GOLES POR PARTIDO FUE DE: {promedio}')
                    l.os.system('pause')
                    
                if (opr=='F'):
                    f.os.system('cls')
                    isReporting=False

###########################################################################################################################################

        if (op==5):
            isApprunning=False