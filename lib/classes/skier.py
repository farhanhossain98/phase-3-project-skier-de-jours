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
        pass

    from classes.event import Event
    from classes.registration import Registration
    from classes.riding_team import RidingTeam