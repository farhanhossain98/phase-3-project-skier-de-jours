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
        if type(new_name) is str and len(new_name) > 0:
            self._name = new_name
        else:
            raise Exception("Name must be greater than 0 characters.")

    from classes.event import Event
    from classes.registration import Registration
    from classes.riding_team import RidingTeam