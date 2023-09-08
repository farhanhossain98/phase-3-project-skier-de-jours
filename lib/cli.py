from classes.event import Event
from classes.registration import Registration
from classes.skier import Skier
from classes.riding_team import RidingTeam

def print_welcome_message():
    print("Welcome to Skier du Jour: The Premiere Skijoring Database")

def print_main_menu() :
    print("+------------------------------+")
    print("|           Main Menu          |")
    print("+------------------------------+")
    print("| Options :                    |")
    print("| 1. View Events               |")
    print("| 2. Skier Information         |")
    print("| 3. Horse & Rider Information |")
    print("| 4. Register to Compete       |")
    print("| e: Exit the program          |")
    print("+------------------------------+")

def print_view_events_menu():
    print("+--------------------------------+")
    print("| Events Menu                    |")
    print("+--------------------------------+")
    print("| Options :                      |")
    print("| 1. Print Event's Registrations |")
    print("| 2. Print Event's Skiers        |")
    print("| 3. Print Event's Riding Teams  |")
    print("| e: Exit Menu                   |")
    print("+--------------------------------+")


def print_skier_info_menu():
    print("+--------------------------------+")
    print("| Skier Information              |")
    print("+--------------------------------+")
    print("| Options :                      |")
    print("| 1. Print Skier's Events        |")
    print("| 2. Print Skier's Registrations |")
    print("| e: Exit Menu                   |")
    print("+--------------------------------+")

def print_riding_team_info_menu():
    print("+--------------------------------------+")
    print("| Horse & Rider Information            |")
    print("+--------------------------------------+")
    print("| Options :                            |")
    print("| 1. Print Riding Team's Events        |")
    print("| 2. Print Riding Team's Registrations |")
    print("| e: Exit Menu                         |")
    print("+--------------------------------------+")

def print_registration_menu():
    print("+-----------------------------+")
    print("| Register to Compete         |")
    print("+-----------------------------+")
    print("| Options :                   |")
    print("| 1. Sign up as a Skier       |")
    print("| 2. Sign up as a Riding Team |")
    print("| 3. Register for an event    |")
    print("| e: Exit Menu                |")
    print("+-----------------------------+") 

        



def view_events_menu():
    looping = True
    while(looping):
        print_view_events_menu()
        command = input("Input your Command :")
        command = command.lower()

        
        if command == "1":
            event_name = input("Input event to search for:")
            try:
                Event.registrations(event_name)
            except TypeError:
                print(f"Could not find event with name: {event_name}")
        
        elif command == "2":
            event_name = input("Input event to search for:")
            try:
                print_event_skiers(event_name)
            except TypeError:
                print(f"Could not find event with name: {event_name}")
       
        elif command == "3":
            event_name = input("Input event to search for:")
            try:
                print_event_riding_teams(event_name)
            except TypeError:
                print(f"Could not find event with name: {event_name}")

# def print_event_registrations():
    # return Event.registrations()
    # pass

def print_event_skiers():
    return Event.skiers()
    pass

def print_event_riding_teams():
    return Event.riding_teams()
    pass


def view_skier_info():
    looping = True
    while(looping):
        print_skier_info_menu()
        print("Input Your Command:   ")
            
        if command == "1":
            skier_name = input("Input skier to search for:")
            try:
                print_skiers_events(skier_name)
            except TypeError:
                print(f"Could not find skier's with name: {skier_name}")

        elif command == "2":
            skier_name = input("Input skier's to search for:")
            try:
                print_skiers_registrations(skier_name)
            except TypeError:
                print(f"Could not find skier's with name: {skier_name}")


def print_skiers_events():
    pass

def print_skiers_registrations():
    pass






def view_riding_team_info():
    looping = True
    while(looping):
        print_riding_team_info_menu()
        print("Input Your Command:   ")
            
        if command == "1":
            riding_team = input("Input riding_team to search for:")
            try:
                print_riding_teams_events(riding_team)
            except TypeError:
                print(f"Could not find riding_team's with name: {riding_team}")

        elif command == "2":
            riding_team = input("Input riding_team's to search for:")
            try:
                print_riding_teams_registrations(riding_team)
            except TypeError:
                print(f"Could not find riding_team's with name: {riding_team}")


def print_riding_teams_events():
    pass

def print_riding_teams_registrations():
    pass




def view_registration_menu():
    looping = True
    while(looping):
        print_registration_menu()
        command = input("Input your Command :")
        command = command.lower()

        if command == "1":
            skier_name = input("Input event to search for:")
            try:
                sign_up_skier(skier_name)
            except TypeError:
                print(f"Could not find event with name: {skier_name}")
        
        elif command == "2":
            riding_team = input("Input event to search for:")
            try:
                sign_up_riding_team(riding_team)
            except TypeError:
                print(f"Could not find event with name: {riding_team}")
        
        elif command == "3":
            event_name = input("Input event to search for:")
            try:
                register_for_event(event_name)
            except TypeError:
                print(f"Could not find event with name: {event_name}")


def sign_up_skier():
    pass

def sign_up_riding_team():
    pass

def register_for_event():
    pass






print_welcome_message()
print_main_menu()
print_view_events_menu()
print_skier_info_menu()
print_riding_team_info_menu()
print_registration_menu()


if __name__ == "__main__":
    print_welcome_message()
    looping = True
    while (looping):
        print_main_menu()
        command = input("What would you like to do: Input: ")
        command = command.lower()

        if command == '1':
            view_events_menu()
        elif command ==  '2':
            view_skier_info()
        elif command == '3':
            view_riding_team_info()
        elif command == '4':
            view_registration_menu()
        elif command == '5':
            looping = False
            print( ' Exiting ')
        else:
            print( ' Please Enter a valid option. ')
        
