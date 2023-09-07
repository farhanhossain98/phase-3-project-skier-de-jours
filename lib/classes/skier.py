class Skier:

    all = []

    def __init__(self, name):
        self.name = name
        Skier.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) is str and 0 < len(new_name) < 15 :
            self._name = new_name
        else:
            raise Exception("Name must be of type string class and between 0-15 characters.")

    @property
    def registration(self):
        return self._registration
    
    @registration.setter
    def registration(self, registration):
        if type(registration) is Registration:
            self._registration = registration
        else:
            raise Exception('Registration must be of Registration class.')


    def events(self):
        return [event for event in Event.all if event.skier is self]
    
    def skiers_registered(self):
        return list (set ( [event.skier for event in self.events()]))


from classes.registration import Registration
from classes.event import Event
from classes.riding_team import RidingTeam
