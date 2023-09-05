class RidingTeam:

    all = []

    def __init__(self,horse_name, rider_name):
        self.horse_name = horse_name
        self.rider_name = rider_name
        RidingTeam.all.append(self)
    

    @property
    def horse_name(self):
        return self._horse_name

    @horse_name.setter
    def horse_name(self, name):
        if type(name) is str:
            if len(name) > 0:
                self._horse_name = name
            else:
                raise ValueError('Name must be more than 0 characters long.')
        else:
            TypeError('Name must be a string.')
        

    @property
    def rider_name(self):
        return self._rider_name
    
    @rider_name.setter
    def rider_name(self, name):
        if type(name) is str:
            if len(name) > 0:
                self._rider_name = name
            else:
                raise ValueError('Name must be more than 0 characters long.')
        else:
            TypeError('Name must be a string.')
        











    from classes.event import Event
    # from classes.registration import Registration
    # from classes.skier import Skier



