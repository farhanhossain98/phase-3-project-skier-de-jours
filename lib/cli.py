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
    Skier.drop_table()    
    Skier.create_table()
    farhan = Skier('farhan')
    hiro = Skier('Hiro')
    farhan.save()
    hiro.save()
    tess = Skier.create("Tess")
    # Skier.get_all()
    print("Intermission")
    # Skier.find_by_name("Hiro")
    # print("Intermission")
    # Skier.find_by_id(1)
    RidingTeam.drop_table()    
    RidingTeam.create_table()
    r1 = RidingTeam('horse1', 'farhan')
    r2 = RidingTeam('horse2','Hiro')
    r1.save()
    r2.save()
    r3 = RidingTeam.create("Bullesye", "Tess")
    # RidingTeam.get_all()
    # print("Intermission")
    # RidingTeam.find_by_rider("Hiro")
    # print("Intermission")
    # RidingTeam.find_by_horse("horse1")
    # print("Intermission")
    # RidingTeam.find_by_id(1)
    Event.drop_table()    
    Event.create_table()
    e1 = Event(1500, 'Dallas')
    e2 = Event(2000,'Philly')
    e1.save()
    e2.save()
    e3 = Event.create(5000, "NYC")
    # Event.get_all()
    # print("Intermission")
    # Event.find_by_location("NYC")
    # print("Intermission")
    # Event.find_by_id(1)
    
    print("location data")
    print("here it goes....")
    Registration.drop_table()    
    Registration.create_table()
    reg1 = Registration(r1.id,farhan.id, e1.id)
    reg2 = Registration(r2.id, hiro.id, e2.id)
    reg1.save()
    reg2.save()
    reg3 = Registration.create(r3.id, tess.id, e3.id)
    Registration.get_all()
    print("Intermission")
    