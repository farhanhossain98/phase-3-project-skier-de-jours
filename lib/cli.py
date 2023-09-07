from classes.event import Event
from classes.registration import Registration
from classes.skier import Skier
from classes.riding_team import RidingTeam

# def main_menu ( ) :

    # task = input("What would you like to do? ")
    # if task == '4' :
        # get_skiers()
    # else :
        # print( 'Please enter valid menu option.')
        # main_menu()

# def get_skiers ( ) :
   

    # main_menu()

task = input( 'would you like to create and show all skiers. Enter : Y/N  ')
if task == 'Y':
    farhan = Skier('farhan')
    hiro = Skier('Hiro')
    farhan.save()
    hiro.save()
    Skier.all()
