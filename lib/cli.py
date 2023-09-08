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
    Skier.get_all()
    print("Intermission")
    # Skier.find_by_name("Hiro")
    # print("Intermission")
    # Skier.find_by_id(1)
    
    #*******************************************
    
    RidingTeam.drop_table()    
    RidingTeam.create_table()
    r1 = RidingTeam('horse1', 'farhan')
    r2 = RidingTeam('horse2','Hiro')
    r1.save()
    r2.save()
    r3 = RidingTeam.create("Bullesye", "Tess")

    #*******************************************

    # print("Riding team get_all:")
    # RidingTeam.get_all()
    # print("Find by rider: hiro")
    # RidingTeam.find_by_rider("Hiro")
    # print("Find by horse: horse1")
    # RidingTeam.find_by_horse("horse1")
    # print("Intermission")
    # RidingTeam.find_by_id(1)
    
    #*******************************************
    
    Event.drop_table()    
    Event.create_table()
    e1 = Event(1500, 'Dallas')
    e2 = Event(2000,'Philly')
    e1.save()
    e2.save()
    e3 = Event.create(5000, "NYC")

    #*******************************************

    # print("Getting all events: ")
    # Event.get_all()
    # print("Find event by location: NYC...")
    # Event.find_by_location("NYC")
    # print("Find event by ID: 1...")
    # Event.find_by_id(1)
    
    #*******************************************

    print("Creating Registrations")
    Registration.drop_table()    
    Registration.create_table()
    test = farhan.create_registration(r2.id, e3.id)
    reg1 = Registration(r1.id,farhan.id, e1.id)
    reg2 = Registration(r2.id, hiro.id, e2.id)
    reg3 = Registration(r1.id,farhan.id, e1.id)
    reg4 = Registration(r2.id,farhan.id, e2.id)
    reg1.save()
    reg2.save()
    reg3 = Registration.create(r3.id, tess.id, e3.id)

    #*******************************************

    print("Get all Registrations")
    Registration.get_all()
    print("Get all of farhans registrations:")
    farhan.registrations()
    print("Get all of farhans events:")
    farhan.events()
    print("Get all of hiro's registrations:")
    hiro.registrations()