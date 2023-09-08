from classes.event import Event
from classes.registration import Registration
from classes.skier import Skier
from classes.riding_team import RidingTeam
from classes.__init__ import seed_database


# db_file = "skijor.db"  # Replace with your database file path
# seed_file = "lib/classes/skijor_seed_db.sql"     # Replace with your seed SQL file path
# seed_database(db_file, seed_file)



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

        #Print event registration
        if command == "1":
            event_name = input("Input event to search for:")
            try:
                print_event_registrations(event_name)
            except TypeError:
                print(f"Could not find event with name: {event_name}")
        #Print event skiers
        elif command == "2":
            event_name = input("Input event to search for:")
            try:
                print_event_skiers(event_name)
            except TypeError:
                print(f"Could not find event with name: {event_name}")
        #Print event riding teams
        elif command == "3":
            event_name = input("Input event to search for:")
            try:
                print_event_riding_teams(event_name)
            except TypeError:
                print(f"Could not find event with name: {event_name}")

print_welcome_message()
print_main_menu()
print_view_events_menu()
print_skier_info_menu()
print_riding_team_info_menu()
print_registration_menu()


def create_new_pet_menu():
    print("Create a new pet:")
    
    name = input("input a name:")
    breed = input("input a breed:")
    age = input("input an age:")
    age = int(age)
    owner_id = input("Input the id of the owner:")
    owner_id = int(owner_id)

    pet = Pet(owner_id, name, breed, age)

    print("Here is the generated pet")
    print_pet_row_header()
    print_pet_row(pet)
    print_pet_row_footer()

    print("Would you like to save it to the database?")
    deciding = True
    while deciding:
        decision = input("(Y/N) :")
        if decision.lower() == "y":
            pet.save()
            deciding = False
            print("Your pet has been created and saved to the database!")
            print("returning to Modify Menu....\n")
        elif decision.lower() == "n":
            print("Pet Creation canceled")
            print("returning to Modify Menu....\n")
            deciding = False
        else:
            print("Decision must be either 'Y' or 'N'")


    # if task == '1' :
    #     get_skiers()
    # else :
    #     print( 'Please enter valid menu option.')
    #     main_menu()

# def get_skiers ( ) :
   

    # main_menu()

# task = input( 'would you like to create and show all skiers. Enter : Y/N  ')
# if task == 'Y':
#     farhan = Skier('farhan')
#     hiro = Skier('Hiro')
#     farhan.save()
#     hiro.save()
#     Skier.all()