class Result:
    all=[]

    def __init__(self, registration, time):
        self.registration = registration
        self.time = time
        Result.all.append(self)
    

    #     self.skier = skier
    #     self.racing_team = racing_team
    #     self.event = event
    #     self.time = time

    # @property
    # def skier(self):
    #     return self._skier
    
    # @skier.setter
    # def skier(self, skier):
    #     if isinstance(skier, Skier):
    #         self._skier = skier

    # @property
    # def racing_team(self):
    #     return self._racing_team
    
    # @racing_team.setter
    # def racing_team(self, racing_team):
    #     if isinstance(racing_team, RidingTeam):
    #         self._racing_team = racing_team

    # @property
    # def event(self):
    #     return self._event
    
    # @event.setter
    # def event(self, event):
    #     if isinstance(event, Event):
    #         self._event = event
    

from classes.event import Event
from classes.registration import Registration
from classes.skier import Skier