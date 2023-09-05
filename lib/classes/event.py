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
    def capacity(self, name):
        pass

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, name):
        pass

# return a list events happening and requirements needed to enter
# return a list of participants 



# 
    # from classes.registration import Registration
    # from classes.riding_team import RidingTeam
    # from classes.skier import Skier
