class Registration:

    all = []

    def __init__(self, riding_team, skier, event):
        self.riding_team = riding_team
        self.skier = skier
        self.event = event
        Registration.all.append(self)

    @property
    def riding_team(self) :
        return self._riding_team
    
    @riding_team.setter
    def riding_team(self, new_team) :
        if type(new_team) is RidingTeam :
            self._riding_team = new_team
        else :
            raise TypeError('Riding team must be of the RidingTeam class.')
        
    @property
    def skier(self):
        return self._skier
    
    @skier.setter
    def skier(self, new_skier):
        if type(new_skier) is Skier:
            self._skier = new_skier
        else:
            raise TypeError('Skier must be of the Skier class')
        
    @property
    def event(self):
        return self._event
    
    @event.setter
    def event(self, new_event):
        if type(new_event) is Event:
            self._event = new_event
        else:
            raise TypeError('Event must be of the Event class')
        
    
    def add_category(self, category):
        category_options = []
        pass


    def add_raw_time(self, raw_time):
        pass

    def add_penalty(self, penalty):
        pass

    
    @property
    def final_time(self, raw_time, penalty):
        return self.final_time

    @final_time.setter
    def final_time(self, raw_time, penalty):
        if not hasattr(self, "final_time"):    
            self._final_time = raw_time + penalty
        else:
            raise Exception("Final time cannot be modified... better luck next year slow poke!")



from classes.event import Event
from classes.riding_team import RidingTeam
from classes.skier import Skier
