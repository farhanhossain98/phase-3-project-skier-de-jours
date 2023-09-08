from classes.event import Event
from classes.registration import Registration
from classes.skier import Skier
from classes.riding_team import RidingTeam
from classes.cli_methods import *

# from classes.__init__ import seed_database
# db_file = "skijor.db"  # Replace with your database file path
# seed_file = "lib/classes/skijor_seed_db.sql"     # Replace with your seed SQL file path
# seed_database(db_file, seed_file)

Skier.drop_table()    
Skier.create_table()
farhan = Skier('farhan')
hiro = Skier('Hiro')
farhan.save()
hiro.save()
tess = Skier.create("Tess")

#*******************************************
    
RidingTeam.drop_table()    
RidingTeam.create_table()
r1 = RidingTeam('horse1', 'farhan')
r2 = RidingTeam('horse2','Hiro')
r1.save()
r2.save()
r3 = RidingTeam.create("Bullesye", "Tess")

#*******************************************    
    
Event.drop_table()    
Event.create_table()
e1 = Event(1500, 'Dallas')
e2 = Event(2000,'Philly')
e1.save()
e2.save()
e3 = Event.create(5000, "NYC")

#*******************************************


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

if __name__ == "__main__":
    print_welcome_message()
    print_main_menu()
    command = input("What would you like to do: Input: ")
    command = command.lower()
    if command == '1':
        Event.get_all()
        
        more_events = input("Would you like to learn more about events? Y/N   ")
        if more_events == "Y":
            print_view_events_menu()
        else:
            print("K thx bye!")

    elif command ==  '2':
        Skier.get_all()
        more_skiers = input("Would you like to learn more about skiers? Y/N   ")
        if more_skiers == "Y":
            print_skier_info_menu()
        else:
            print("K thx bye!")

    elif command == '3':
        RidingTeam.get_all()
        more_riding_teams = input("Would you like to learn more about the riding teams? Y/N   ")
        if more_riding_teams == "Y":
            print_riding_team_info_menu()
        else:
            print("K thx bye!")
    elif command == '4':
        Registration.get_all()
        more_registrations = input("Would you like to learn more about registering? Y/N   ")
        if more_registrations == "Y":
            print_registration_menu()
        else:
            print("K thx bye!")
    elif command == '5':
        looping = False
        print( ' Exiting... bye, bye, bye! ')
    else:
        print( ' Please Enter a valid option. ')
    



    # print_welcome_message()
    # looping = True
    # while (looping):
    #     print_main_menu()
    #     command = input("What would you like to do: Input: ")
    #     command = command.lower()

    #     if command == '1':
    #         Event.get_all()
    #     elif command ==  '2':
    #         view_skier_info()
    #     elif command == '3':
    #         view_riding_team_info()
    #     elif command == '4':
    #         view_registration_menu()
    #     elif command == '5':
    #         looping = False
    #         print( ' Exiting ')
    #     else:
    #         print( ' Please Enter a valid option. ')
        

# Skier.get_all()
# print("Intermission")
# Skier.find_by_name("Hiro")
# print("Intermission")
# Skier.find_by_id(1)
    
# print("Riding team get_all:")
# RidingTeam.get_all()
# print("Find by rider: hiro")
# RidingTeam.find_by_rider("Hiro")
# print("Find by horse: horse1")
# RidingTeam.find_by_horse("horse1")
# print("Intermission")
# RidingTeam.find_by_id(1)

 
# print("Getting all events: ")
# Event.get_all()
# print("Find event by location: NYC...")
# Event.find_by_location("NYC")
# print("Find event by ID: 1...")
# Event.find_by_id(1)
    

# print("Get all Registrations")
# Registration.get_all()
# print("Get all of farhans registrations:")
# farhan.registrations()
# print("Get all of farhans events:")
# farhan.events()
# print("Get all of hiro's registrations:")
# hiro.registrations()


