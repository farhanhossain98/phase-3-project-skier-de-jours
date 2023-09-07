class Event:

    all = []

    def __init__(self, capacity, location):
        self.capacity = capacity 
        self.location = location
        Event.all.append(self)

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    # attendee < capacity 
    def capacity(self, capacity):
        if type(capacity) is int and not hasattr(self, "capacity"):
            self._capacity = capacity
        else: 
            raise Exception("Capacity has to be an integer.")

    @property
    def location(self):
        return self._location
    
    @location.setter
    # states will have elements and if our location requirements are met by the state it is ok to hold an event 
    def location(self, name):
        if type(name) is str:
            if len(name) > 0:
                self._location = name
            else:
                raise ValueError('Name must be more than 0 characters long.')
        else:
            TypeError('Name must be a string.')

# return number of attendees
# return a list events happening and requirements needed to enter
# return a list of participants 

from classes.registration import Registration
from classes.riding_team import RidingTeam
from classes.skier import Skier
