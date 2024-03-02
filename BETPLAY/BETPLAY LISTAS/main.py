import modulos.menu as mp
import modulos.menuReportes as mr
import modulos.equipos as e
import modulos.fechas as f
if __name__ == '__main__':
    equiposLiga = []
    fecha=[[],[],[],[],[],[],[],[],[],[],[],[]]
    isAppRunning = True
    while isAppRunning:
        op=mp.CrearMenu()
        if (op ==1):
            isAddTeam = True
            while isAddTeam:
                e.os.system('cls')
                e.AddTeam(equiposLiga)
                isAddTeam = bool(input('Desea agregar otro Equipo S(Si) o Enter(No)'))
        elif (op ==2):
            e.viewTeams(equiposLiga)
        elif (op ==3):
            f.AddGame(equiposLiga,fecha)
        elif (op ==4):
             isReport = True
             while isReport:
                 opr = mr.CrearMenu()
                 if (opr == 'A'):
                     pass
                 elif (opr == 'B'):
                     pass
                 elif (opr == 'F'):
                     isReport = False

        elif (op ==5):
            isAppRunning=False 