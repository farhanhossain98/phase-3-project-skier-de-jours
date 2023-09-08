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

# task = input( 'would you like to create and show all skiers. Enter : Y/N  ')
# if task == 'Y':
    # Skier.create_table()
    # farhan = Skier('farhan')
    # hiro = Skier('Hiro')
    # farhan.save()
    # hiro.save()
    # Skier.get_all()


task = input ( ' would you like to createa and show all riding teams. Enter: Y/N   ')
if task == 'Y':
    RidingTeam.drop_table()
    RidingTeam.create_table()
    r1 = RidingTeam('Sugar', 'Tess')
    r1.save()
    r2 = RidingTeam.create('bullseye','hiroki')
    r3 = RidingTeam.create('happy','farhan')
    RidingTeam.get_all()
    print('Line break')


    RidingTeam.find_by_rider_name('Tess')
    RidingTeam.find_by_id('1')